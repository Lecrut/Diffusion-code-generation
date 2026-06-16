from collections import defaultdict
def group_fruits(fruit_list):
    family_map = {
        "apple": ["Rosaceae"],
        "banana": ["Musaceae"],
        "cherry": ["Rosaceae"],
        "date": ("Polygonoideae",),
        "grape": ["Vitaceae"],
        "kiwi": ["Actinidiaceae"],
        "lemon": ["Rutaceae"],
        "mango": ["Anacardiaceae"],
        "orange": ["Rutaceae"],
        "peach": ["Rosaceae"],
    }
    grouped = defaultdict(list)
    for fruit in fruit_list:
        if fruit.lower() in family_map:
            fams = family_map[fruit.lower()]
            for f in fams:
                grouped[f].append(fruit)
        else:
            grouped["Other"].append(fruit)
    return dict(grouped)
if __name__ == '__main__':
    fruits = ["apple", "banana", "cherry", "date", "grape", "kiwi", 
              "lemon", "mango", "orange", "peach", "pear"]
    result = group_fruits(fruits)
    for family, fruit_list in sorted(result.items()):
        print(f"{family}: {fruit_list}")