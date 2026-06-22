def get_first_element(lst):
    return lst[0] if lst else None

if __name__ == '__main__':
    sample_data = {
        'numbers': [1, 2, 3],
        'empty': [],
        'strings': ['apple', 'banana', 'cherry'],
        'mixed': [42, 3.14, 'hello', True]
    }
    for category, lst in sample_data.items():
        print(f"First element of {category}: {get_first_element(lst)}")