import re
from collections import defaultdict
def group_and_sort_fruits(fruit_list):
    suffix_pattern = r'(apple|orange|banana|mango)'
    grouped_data = {}
    for fruit in fruit_list:
        match = re.search(suffix_pattern, fruit.lower())
        if not match:
            continue
        category = match.group(1)
        if category not in grouped_data:
            grouped_data[category] = []
        grouped_data[category].append(fruit)
    sorted_groups = {}
    for category, fruits in grouped_data.items():
        sorted_fruits = sorted(fruits)
        if not isinstance(sorted_fruits, list):
            continue
        sorted_groups[category] = sorted_fruits
    return sorted_groups
if __name__ == '__main__':
    sample_data = [
        'Red Apple',
        'Green Orange',
        'Yellow Banana',
        'Pink Mango',
        'Blue Apple Pie',
        'Orange Juice',
        'Banana Split',
        'Mango Lassi'
    ]
    result = group_and_sort_fruits(sample_data)
    for category, items in result.items():
        print(f"{category}: {items}")