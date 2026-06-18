def parse_fruit_input(input_string):
    return [fruit.strip() for fruit in input_string.split(',')]
def categorize_fruits(fruits_list):
    categories = {
        'Citrus': [],
        'Berry': [],
        'Tropical': []
    }
    for fruit in fruits_list:
        if any(word.lower() in fruit.lower() for word in ['orange', 'lemon', 'lime']):
            categories['Citrus'].append(fruit)
        elif any(word.lower() in fruit.lower() for word in ['strawberry', 'blueberry', 'raspberry']):
            categories['Berry'].append(fruit)
        else:
            categories['Tropical'].append(fruit)
    return categories
if __name__ == '__main__':
    sample_input = "apple, orange, banana, strawberry, mango, lemon"
    fruits = parse_fruit_input(sample_input)
    grouped = categorize_fruits(fruits)
    for category_name, items in grouped.items():
        print(f"{category_name}: {', '.join(items)}")