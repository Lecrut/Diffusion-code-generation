from collections import defaultdict
def group_fruits(fruit_list):
    family_map = {
        "apple": ["Rosaceae", "Fruiting"],
        "banana": ["Musaceae", "Tropical"],
        "cherry": ["Rosaceae", "Berry"],
        "date": ["Moraceae", "Drought-tolerant"],
        "grape": ["Vitaceae", "Vine"],
        "lemon": ["Rutaceae", "Citrus"],
        "mango": ["Anacardiaceae", "Tropical"],
    }
    grouped = defaultdict(list)
    for fruit in fruit_list:
        if fruit.lower() in family_map:
            name, type_ = family_map[fruit.lower()]
            grouped[name].append(fruit)
            grouped[type_].append(fruit)
    return dict(grouped)
if __name__ == '__main__':
    fruits = ["apple", "banana", "cherry", "date", "grape", "lemon", "mango"]
    result = group_fruits(fruits)
    print(result)