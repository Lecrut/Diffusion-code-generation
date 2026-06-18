def parse_fruit_input(input_string):
    return [fruit.strip() for fruit in input_string.split(',') if fruit.strip()]
def categorize_fruits(fruits_list, classification_rules):
    categorized = {}
    def get_category(fruit_name):
        name_lower = fruit_name.lower()
        if 'apple' in name_lower or 'pear' in name_lower:
            return 'Pome Fruits'
        elif 'banana' in name_lower or 'mango' in name_lower:
            return 'Tropical/Banana Family'
        else:
            return 'Other Fruit'
    for fruit in fruits_list:
        category = get_category(fruit)
        if category not in categorized:
            categorized[category] = []
        categorized[category].append(fruit)
    return categorized
if __name__ == '__main__':
    sample_input = "apple, banana, orange, mango, pear"
    fruits = parse_fruit_input(sample_input)
    groups = categorize_fruits(fruits, None)
    for category, fruit_list in sorted(groups.items()):
        print(f"{category}: {', '.join(fruit_list)}")