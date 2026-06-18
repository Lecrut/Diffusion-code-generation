import re
from collections import defaultdict
def group_and_sort_fruits(fruit_list):
    suffix_pattern = r'(apple|orange|banana|mango)'
    grouped_data = defaultdict(list)
    for fruit in fruit_list:
        match = re.search(suffix_pattern, fruit.lower())
        if not match:
            continue
        category_name = match.group(1).capitalize()
        normalized_suffix = f"{category_name} Group"
        grouped_data[normalized_suffix].append(fruit)
    sorted_groups = {}
    for category, fruits in grouped_data.items():
        sorted_fruits = sorted(fruits)
        sorted_groups[category] = sorted_fruits
    return dict(sorted_groups)
if __name__ == '__main__':
    sample_fruits = [
        "Red Apple",
        "Green Orange",
        "Yellow Banana",
        "Sweet Mango",
        "Big Red Apple",
        "Juicy Orange",
        "Banana Split",
        "Mango Lassi"
    ]
    result = group_and_sort_fruits(sample_fruits)
    print(result)