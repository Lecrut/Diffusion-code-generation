def get_first_element(data):
    return data[0]

if __name__ == '__main__':
    sample_lists = {
        'numbers': [1, 2, 3, 4],
        'letters': ['a', 'b', 'c'],
        'empty': []
    }
    
    for name, lst in sample_lists.items():
        try:
            print(f"First element of {name} list: {get_first_element(lst)}")
        except IndexError as e:
            print(f"Caught expected error for empty {name} list: {e}")