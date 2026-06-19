def get_first_element(data):
    try:
        return data[0]
    except IndexError:
        return None

if __name__ == '__main__':
    sample_values = {
        'list1': [5, 10, 15],
        'list2': ['a', 'b', 'c'],
        'empty_list': [],
        'single_element': [42]
    }
    
    for key, value in sample_values.items():
        first_element = get_first_element(value)
        print(f"First element of {key}: {first_element}")