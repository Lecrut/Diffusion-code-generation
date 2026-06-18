from collections import defaultdict
def group_fruits(fruit_list):
    family_map = {
        "apple": ["Rosaceae", "Apple"],
        "banana": ["Musaceae", "Bananaceous"],
        "grape": ["Vitaceae", "Grapevine"],
        "orange": ["Rutaceae", "Citrus"],
        "cherry": ["Rosaceae", "Prunus"],
        "peach": ["Rosaceae", "Amygdalaceae"],
    }
    grouped = defaultdict(list)
    for fruit in fruit_list:
        if fruit.lower() in family_map:
            name, fam = family_map[fruit.lower()]
            grouped[name].append(fruit)
            grouped[fam].append(fruit)
        return dict(grouped)
if __name__ == '__main__':
    fruits = ["apple", "banana", "grape", "orange", "cherry", "peach"]
    result = group_fruits(fruits)
    for key, value in sorted(result.items()):
        print(key + ": " + str(value))