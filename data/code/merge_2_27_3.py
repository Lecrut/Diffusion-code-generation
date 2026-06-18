def parse_fruit_input(input_string):
    return [fruit.strip() for fruit in input_string.split(',') if fruit.strip()]
def classify_fruits(fruits_list, classification_rules):
    groups = {}
    def get_category(fruit_name):
        name_lower = fruit_name.lower().strip()
        if 'orange' in name_lower or 'lemon' in name_lower:
            return 'Citrus'
        elif any(berry in name_lower for berry in ['strawberry', 'blueberry']):
            return 'Berries'
        elif any(tropical in name_lower for tropical in ['mango', 'pineapple']):
            return 'Tropical'
        else:
            return 'Other'
    for fruit in fruits_list:
        category = get_category(fruit)
        if category not in groups:
            groups[category] = []
        groups[category].append(fruit)
    return groups
if __name__ == '__main__':
    sample_input = "apple, orange, strawberry, mango, banana, lemon"
    classification_rules = {
        'rule_1': ['orange', 'lemon'],
        'rule_2': ['strawberry', 'blueberry'],
        'rule_3': ['mango', 'pineapple']
    }
    parsed_fruits = parse_fruit_input(sample_input)
    categorized_groups = classify_fruits(parsed_fruits, classification_rules)
    for category in sorted(categorized_groups.keys()):
        print(f"{category}: {categorized_groups[category]}")