def map_category(input_string: str) -> str:
    category_map = {'apple': lambda x: 'Fruit', 'carrot': lambda x: 'Vegetable', 'banana': lambda x: 'Fruit', 'spinach': lambda x: 'Vegetable'}
    return category_map.get(input_string.lower(), lambda x: 'Unknown')('')
if __name__ == '__main__':
    sample_input_1 = 'Apple'
    sample_input_2 = 'Spinach'
    sample_input_3 = 'Grape'
    print(map_category(sample_input_1))
    print(map_category(sample_input_2))
    print(map_category(sample_input_3))