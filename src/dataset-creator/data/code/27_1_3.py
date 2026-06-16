from collections import defaultdict
def group_fruits(fruit_list):
    family_map = {
        "apple": ["Rosaceae", "Apple"],
        "banana": ["Musaceae", "Banana"],
        "orange": ["Rutaceae", "Citrus"],
        "grape": ["Vitaceae", "Vitis"],
        "peach": ["Rosaceae", "Peach"],
        "mango": ["Anacardiaceae", "Mangifera"],
        "strawberry": ["Rosales", "Fragaria"],
        "pineapple": ["Bromeliaceae", "Ananas"]
    }
    grouped = defaultdict(list)
    for fruit in fruit_list:
        if fruit.lower() in family_map:
            name, fam = family_map[fruit.lower()]
            grouped[name].append(fruit)
            grouped[fam].append(fruit)
    return dict(grouped)
if __name__ == '__main__':
    fruits = ["apple", "banana", "orange", "grape", "peach", "mango", "strawberry", "pineapple"]
    result = group_fruits(fruits)
    print(result)