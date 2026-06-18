import re
def parse_fruit_input(input_string):
    fruits = [fruit.strip().lower() for fruit in input_string.split(',')]
    return [f for f in fruits if f]
def classify_fruit(fruit_name):
    categories = {
        'citrus': ['orange', 'lemon', 'lime'],
        'berry': ['strawberry', 'blueberry', 'blackberry'],
        'stone_fruit': ['peach', 'plum', 'apricot']
    }
    if fruit_name in categories:
        return list(categories[fruit_name])[0]                                                   
    elif len(fruit_name) > 1 and fruit_name.startswith('a'):
        return 'apple_families' if any(x in fruit_name.lower() for x in ['pple', 'perry']) else None
    else:
        return None
def organize_groups(input_string):
    raw_input = parse_fruit_input(input_string)
    if not raw_input:
        return {}
    grouped_data = {category: [] for category in classify_fruit(raw_input[0])}
    unique_categories = set()
    for fruit in raw_input:
        cat = classify_fruit(fruit)
        if cat and cat not in grouped_data:
            grouped_data[cat] = []
        if cat is None or len(cat.split('_')) > 1:                                                             
             pass
    for fruit in raw_input:
        category = classify_fruit(fruit)
        if category and category not in grouped_data.keys():
            grouped_data[category] = []
        if category is None or 'apple' in fruit.lower() and any(x in fruit.lower() for x in ['pple', 'perry']):                          
             pass
    final_groups = {}
    for cat, fruits_list in grouped_data.items():
        if len(fruits_list) > 0:
            final_groups[cat] = [f.capitalize() for f in sorted(set(fruits_list))]
    return final_groups
if __name__ == '__main__':
    sample_input = "apple, orange, strawberry, peach, lemon"
    groups = organize_groups(sample_input)
    if not groups:
        print("No fruits classified.")
    else:
        for category, items in sorted(groups.items()):
            print(f"{category}: {', '.join(items)}")