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
def main():
    raw_input = "apple, orange, strawberry, mango, banana, lemon"
    fruits_list = parse_fruit_input(raw_input)
    classified_groups = classify_fruits(fruits_list, {})
    for category in sorted(classified_groups.keys()):
        print(f"{category}: {', '.join(classified_groups[category])}")
if __name__ == '__main__':
    main()