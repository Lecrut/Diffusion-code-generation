def parse_fruit_input(input_string):
    return [fruit.strip() for fruit in input_string.split(',') if fruit.strip()]
def categorize_fruits(fruits_list, classification_rules):
    categorized = {}
    def get_category(fruit_name):
        name_lower = fruit_name.lower()
        if 'red' in name_lower or 'apple' == name_lower:
            return 'Red Fruits'
        elif 'green' in name_lower or 'lime' == name_lower:
            return 'Green Fruits'
        else:
            return 'Other Fruits'
    for fruit in fruits_list:
        category = get_category(fruit)
        if category not in categorized:
            categorized[category] = []
        categorized[category].append(fruit)
    return categorized
def main():
    raw_input = "apple, banana, orange, strawberry, lime"
    fruits = parse_fruit_input(raw_input)
    groups = categorize_fruits(fruits, {})
    for category, fruit_list in groups.items():
        print(category + ":")
        for item in fruit_list:
            print("- " + item)
if __name__ == '__main__':
    main()