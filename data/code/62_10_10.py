def get_second_item(lst):
    try:
        return lst[1]
    except IndexError:
        return None

if __name__ == '__main__':
    sample_data = {
        'list_a': [1, 2, 3],
        'list_b': ['a', 'b'],
        'list_c': [True, False, True],
        'list_d': [],
        'list_e': [42]
    }
    
    for key, value in sample_data.items():
        result = get_second_item(value)
        print(f"The second item in {key} is: {result}")