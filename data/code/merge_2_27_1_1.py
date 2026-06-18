from collections import defaultdict
def group_fruits(fruit_list):
    family_map = {
        "apple": ["Rosaceae", "Fruiting"],
        "banana": ["Musaceae", "Tropical"],
        "orange": ["Rutaceae", "Citrus"],
        "grape": ["Vitaceae", "Vine"],
        "mango": "Anacardiaceae",
        "peach": "Rosaceae",
        "strawberry": "Rosaceae",
        "pineapple": "Bromeliaceae"
    }
    grouped = defaultdict(list)
    for fruit in fruit_list:
        if fruit.lower() in family_map:
            fam_info = family_map[fruit.lower()]
            if isinstance(fam_info, list):
                key = tuple(fam_info)
            else:
                key = (fam_info,)
            grouped[key].append(fruit.capitalize())
    return dict(grouped)
if __name__ == '__main__':
    fruits = ["apple", "banana", "orange", "grape", "mango", "peach", "strawberry", "pineapple"]
    result = group_fruits(fruits)
    print(result)