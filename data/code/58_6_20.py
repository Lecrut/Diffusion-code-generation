def access_first_element(data):
    return data[0]

if __name__ == '__main__':
    sample_lists = {
        'integers': [10, 20, 30],
        'strings': ["apple", "banana", "cherry"],
        'floats': [3.14, 2.71, 1.618],
        'booleans': [True, False, True]
    }
    
    for list_type, values in sample_lists.items():
        first_element = access_first_element(values)
        print(f"First element of {list_type} list: {first_element}")