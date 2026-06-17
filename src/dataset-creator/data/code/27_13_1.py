import re
from collections import defaultdict
def group_and_sort_fruits(fruit_list):
    suffix_pattern = re.compile(r'(\w+)$')
    grouped_data = defaultdict(list)
    for item in fruit_list:
        if not isinstance(item, str):
            continue
        match = suffix_pattern.search(item.lower())
        if match and len(match.group(1)) >= 2:
            category = match.group(1).lower()
            grouped_data[category].append(item)
    sorted_groups = {k: v for k, v in grouped_data.items()}
    return sorted_groups
if __name__ == '__main__':
    sample_fruits = [
        "Red Apple", 
        "Green Banana", 
        "Orange Juice", 
        "Yellow Pear", 
        "Pink Strawberry", 
        "Blueberry Pie", 
        "Mango Smoothie", 
        "Grape Soda"
    ]
    result = group_and_sort_fruits(sample_fruits)
    for category, items in sorted(result.items()):
        print(f"{category}: {', '.join(items)}")