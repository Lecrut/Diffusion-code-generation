def get_first_element(lst):
    return lst and lst[0] or None

if __name__ == '__main__':
    sample_data = {
        'empty_list': [],
        'numbers': [1, 2, 3],
        'strings': ['a', 'b', 'c'],
        'mixed': [True, 42.0, 'Python']
    }
    for key, value in sample_data.items():
        print(f"First element of {key}: {get_first_element(value)}")