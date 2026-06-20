def categorize_string(input_string: str) -> str:
    category_rules = {
        'apple': lambda x: 'Fruit',
        'carrot': lambda x: 'Vegetable',
        'water': lambda x: 'Liquid',
        'fire': lambda x: 'Element'
    }
    return next((rule(input_string) for rule in category_rules.values() if input_string in category_rules), "Unknown")

if __name__ == '__main__':
    sample_input_1 = 'apple'
    sample_input_2 = 'fire'
    print(categorize_string(sample_input_1))
    print(categorize_string(sample_input_2))