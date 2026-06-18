import sys
def group_fruits(fruit_list):
    family_map = {
        "apple": ("Rosaceae", 1),
        "banana": ("Musaceae", 2),
        "orange": ("Rutaceae", 3),
        "grape": ("Vitaceae", 4),
        "peach": ("Rosaceae", 5),
        "mango": ("Anacardiaceae", 6),
        "pineapple": ("Bromeliaceae", 7),
        "strawberry": ("Rosales", 8)
    }
    grouped = {}
    for fruit in fruit_list:
        if fruit.lower() not in family_map:
            continue
        key, value = family_map[fruit.lower()]
        if key not in grouped:
            grouped[key] = []
        grouped[key].append(fruit)
    return grouped
if __name__ == '__main__':
    fruits = ["apple", "banana", "orange", "grape", "peach", "mango", "pineapple", "strawberry"]
    result = group_fruits(fruits)
    for family, members in sorted(result.items()):
        print(f"{family}: {members}")