def map_to_category(input_string: str) -> str:
    category_map = {'apple': lambda x: 'fruit', 'carrot': lambda x: 'vegetable', 'banana': lambda x: 'fruit', 'spinach': lambda x: 'vegetable'}
    return category_map.get(input_string, lambda x: 'unknown')(input_string)
if __name__ == '__main__':
    print(map_to_category('apple'))
    print(map_to_category('carrot'))
    print(map_to_category('banana'))
    print(map_to_category('spinach'))
    print(map_to_category('grape'))