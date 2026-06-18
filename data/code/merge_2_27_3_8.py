def parse_fruit_input(input_string):
    return [fruit.strip().lower() for fruit in input_string.split(',') if fruit.strip()]
def categorize_fruits(fruits_list, classification_rules):
    categorized = {}
    def apply_rule(rule_name, rule_func):
        return {rule_name: [fruit for fruit in fruits_list if rule_func(fruit)]}
    has_seed = lambda f: 'seed' in f
    categorized['citrus_with_seeds'] = apply_rule('Citrus with Seeds', has_seed)
    categorized['red_fruits'] = apply_rule('Red Fruits', lambda f: f.startswith(('apple', 'strawberry')))
    return categorized
def main():
    raw_input = "Apple, Banana, Orange, Strawberry, Watermelon, Grape"
    fruits = parse_fruit_input(raw_input)
    groups = categorize_fruits(fruits, {})                                                                           
    print("Fruit Groups:")
    for category_name, group_items in sorted(groups.items()):
        if group_items:
            print(f"{category_name}: {', '.join(group_items)}")
if __name__ == '__main__':
    main()