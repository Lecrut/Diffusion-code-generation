def get_first_element(lst):
    try:
        return lst[0]
    except IndexError:
        return None

if __name__ == '__main__':
    sample_values = {
        'list1': [1, 2, 3],
        'list2': [],
        'list3': ['apple', 'banana', 'cherry']
    }
    
    for key, value in sample_values.items():
        print(f"First element of {key}: {get_first_element(value)}")