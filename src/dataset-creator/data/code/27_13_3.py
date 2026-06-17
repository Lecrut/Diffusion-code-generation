import re
from collections import defaultdict
def group_and_sort_fruits(fruit_list):
    suffix_pattern = r'^(.+?)$'                                          
    grouped_data = defaultdict(list)
    for item in fruit_list:
        if isinstance(item, str):
            clean_name = re.sub(r'[^\w\s]', '', item.lower())
            parts = clean_name.split()
            suffixes_to_check = []
            if len(parts) > 1:
                potential_suffix = parts[-1]
                for suffix_candidate in ['apple', 'orange', 'banana', 'grape']:
                    if item.lower().endswith(suffix_candidate):
                        grouped_data[suffix_candidate].append(item)
                        break
                else:
                     for suffix in ['apple', 'orange', 'banana', 'grape']:
                         if item.lower().startswith(suffix):
                             grouped_data[suffix].append(item)
                             break
    return dict(grouped_data)
def main():
    sample_fruits = [
        "Red Apple", 
        "Green Orange", 
        "Yellow Banana", 
        "Purple Grape", 
        "Sweet Orange", 
        "Big Red Apple", 
        "Small Yellow Banana"
    ]
    grouped_result = group_and_sort_fruits(sample_fruits)
    for category in sorted(grouped_result.keys()):
        fruits_in_category = sorted(grouped_result[category])
        print(f"{category}:")
        for fruit in fruits_in_category:
            print(fruit)
if __name__ == '__main__':
    main()