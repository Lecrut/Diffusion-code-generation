def categorize_string(input_string: str) -> tuple:
    category_map = {'apple': lambda s: ('Fruit', 'Sweet'), 'carrot': lambda s: ('Vegetable', 'Orange'), 'banana': lambda s: ('Fruit', 'Yellow'), 'spinach': lambda s: ('Vegetable', 'Green')}
    if input_string.lower() in category_map:
        return category_map[input_string.lower()](input_string)
    else:
        return ('Unknown', 'Category not found')
if __name__ == '__main__':
    sample_input_1 = 'Apple'
    sample_input_2 = 'Carrot'
    sample_input_3 = 'Banana'
    sample_input_4 = 'Spinach'
    sample_input_5 = 'Grape'
    print(categorize_string(sample_input_1))
    print(categorize_string(sample_input_2))
    print(categorize_string(sample_input_3))
    print(categorize_string(sample_input_4))
    print(categorize_string(sample_input_5))