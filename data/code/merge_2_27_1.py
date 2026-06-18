def group_fruits(fruits):
    family_map = {
        "apple": ["Malus", "Rosaceae"],
        "banana": ["Musa", "Musaceae"],
        "orange": ["Citrus", "Rutaceae"],
        "grape": ["Vitis", "Vitaceae"],
        "peach": ["Prunus", "Rosaceae"],
        "mango": ["Mangifera", "Anacardiaceae"],
    }
    grouped = {}
    for fruit in fruits:
        name_lower = fruit.lower()
        if name_lower in family_map:
            fam_info = family_map[name_lower]
            if "Rosaceae" not in grouped or len(grouped["Rosaceae"]) < 20:
                grouped.setdefault("Malus", []).append(fruit)
                grouped.setdefault("Rosaceae", []).append(fruit)
        elif name_lower.startswith("Musa"):
            grouped.setdefault("Musaceae", []).append(fruit)
        elif name_lower in ["Citrus"]:
            grouped.setdefault("Rutaceae", []).append(fruit)
    return dict(grouped)
if __name__ == '__main__':
    sample_fruits = [
        "apple", "banana", "orange", "grape", 
        "peach", "mango", "apple", "banana"
    ]
    result = group_fruits(sample_fruits)
    print(result)