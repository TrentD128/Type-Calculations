type_chart = {
    "Normal": {"weaknesses": ["Fighting"], "resistances": [], "immunities": ["Ghost"]},
    "Fire": {"weaknesses": ["Water", "Ground", "Rock"], "resistances": ["Fire", "Grass", "Ice", "Bug", "Steel", "Fairy"], "immunities": []},
    "Water": {"weaknesses": ["Electric", "Grass"], "resistances": ["Fire", "Water", "Ice", "Steel"], "immunities": []},
    "Electric": {"weaknesses": ["Ground"], "resistances": ["Electric", "Flying", "Steel"], "immunities": []},
    "Grass": {"weaknesses": ["Fire", "Ice", "Poison", "Flying", "Bug"], "resistances": ["Water", "Electric", "Grass", "Ground"], "immunities": []},
    "Ice": {"weaknesses": ["Fire", "Fighting", "Rock", "Steel"], "resistances": ["Ice"], "immunities": []},
    "Fighting": {"weaknesses": ["Flying", "Psychic", "Fairy"], "resistances": ["Bug", "Rock", "Dark"], "immunities": []},
    "Poison": {"weaknesses": ["Ground", "Psychic"], "resistances": ["Grass", "Fighting", "Poison", "Bug", "Fairy"], "immunities": []},
    "Ground": {"weaknesses": ["Water", "Ice", "Grass"], "resistances": ["Poison", "Rock"], "immunities": ["Electric"]},
    "Flying": {"weaknesses": ["Electric", "Ice", "Rock"], "resistances": ["Grass", "Fighting", "Bug"], "immunities": ["Ground"]},
    "Psychic": {"weaknesses": ["Bug", "Ghost", "Dark"], "resistances": ["Fighting", "Psychic"], "immunities": []},
    "Bug": {"weaknesses": ["Fire", "Flying", "Rock"], "resistances": ["Grass", "Fighting", "Ground"], "immunities": []},
    "Rock": {"weaknesses": ["Water", "Grass", "Ice", "Fighting", "Ground", "Steel"], "resistances": ["Normal", "Fire", "Poison", "Flying"], "immunities": []},
    "Ghost": {"weaknesses": ["Ghost", "Dark"], "resistances": ["Poison", "Bug"], "immunities": ["Normal", "Fighting"]},
    "Dragon": {"weaknesses": ["Ice", "Dragon", "Fairy"], "resistances": ["Fire", "Water", "Electric", "Grass"], "immunities": []},
    "Dark": {"weaknesses": ["Fighting", "Bug", "Fairy"], "resistances": ["Ghost", "Dark"], "immunities": ["Psychic"]},
    "Steel": {"weaknesses": ["Fire", "Fighting", "Ground"], "resistances": ["Normal", "Grass", "Ice", "Flying", "Psychic", "Bug", "Dragon", "Steel", "Fairy"], "immunities": ["Poison"]},
    "Fairy": {"weaknesses": ["Poison", "Steel"], "resistances": ["Fighting", "Bug", "Dark"], "immunities": ["Dragon"]}
}

def dual_type_matchup(type1, type2):
    weaknesses = set(type_chart[type1]["weaknesses"] + type_chart[type2]["weaknesses"])
    resistances = set(type_chart[type1]["resistances"] + type_chart[type2]["resistances"])
    immunities = set(type_chart[type1]["immunities"] + type_chart[type2]["immunities"])

    # Removing weaknesses and resistances that are in immunities
    weaknesses = weaknesses - immunities
    resistances = resistances - immunities

    # Removing overlapping weaknesses and resistances
    overlapping = weaknesses & resistances
    weaknesses = weaknesses - overlapping
    resistances = resistances - overlapping

    return {"weaknesses": sorted(weaknesses), "resistances": sorted(resistances), "immunities": sorted(immunities)}

types = list(type_chart.keys())

for i in range(len(types)):
    for j in range(i, len(types)):
        type1 = types[i]
        type2 = types[j]

        matchup = dual_type_matchup(type1, type2)

        # Print all weaknesses, resistances, and immunities for the dual type combination
        print(f"{type1}/{type2}:")
        print(f"  Weak to: {', '.join(matchup['weaknesses'])} ({len(matchup['weaknesses'])} weaknesses)")
        print(f"  Resistant to: {', '.join(matchup['resistances'])} ({len(matchup['resistances'])} resistances)")
        print(f"  Immune to: {', '.join(matchup['immunities'])} ({len(matchup['immunities'])} immunities)")

        # Check for 4x effective and 0.25x effective type combinations
        for t in types:
            if t in matchup['weaknesses']:
                if type_chart[t]["weaknesses"]:
                    if set(type_chart[t]["weaknesses"]).issubset(set(matchup['weaknesses'])):
                        print(f"    4x effective against: {t}")
            if t in matchup['resistances']:
                if type_chart[t]["resistances"]:
                    if set(type_chart[t]["resistances"]).issubset(set(matchup['resistances'])):
                        print(f"    0.25x effective against: {t}")
