import re
from collections import defaultdict
def group_and_sort_fruits(fruit_list):
    suffix_pattern = re.compile(r'(\w+)$')
    grouped_fruits = defaultdict(list)
    for fruit in fruit_list:
        match = suffix_pattern.match(fruit.lower())
        if not match:
            continue
        group_key = match.group(1).strip()
        grouped_fruits[group_key].append(fruit)
    for category in grouped_fruits:
        grouped_fruits[category] = sorted(grouped_fruits[category])
    return dict(grouped_fruits)
if __name__ == '__main__':
    sample_data = [
        "Apple", 
        "banana", 
        "Orange", 
        "grapefruit", 
        "apple pie", 
        "orange juice", 
        "mango", 
        "strawberry"
    ]
    result = group_and_sort_fruits(sample_data)
    for category, sorted_items in result.items():
        print(f"{category}: {sorted_items}")