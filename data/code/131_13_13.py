def categorize_input(input_string: str) -> tuple:
    category_mapping = {
        'apple': lambda x: ('Fruit', 'Red'),
        'banana': lambda x: ('Fruit', 'Yellow'),
        'carrot': lambda x: ('Vegetable', 'Orange'),
        'dog': lambda x: ('Animal', 'Bark'),
        'elephant': lambda x: ('Animal', 'Trunk')
    }
    
    category = category_mapping.get(input_string.lower())
    if category:
        return category(input_string)
    else:
        raise ValueError("Invalid input string")

if __name__ == '__main__':
    sample_input_1 = 'Apple'
    sample_input_2 = 'Banana'
    sample_input_3 = 'Carrot'
    sample_input_4 = 'Dog'
    sample_input_5 = 'Elephant'

    print(categorize_input(sample_input_1))
    print(categorize_input(sample_input_2))
    print(categorize_input(sample_input_3))
    print(categorize_input(sample_input_4))
    print(categorize_input(sample_input_5))