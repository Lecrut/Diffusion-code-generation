def get_first_element(data):
    if not data:
        return None
    return data[0]

if __name__ == '__main__':
    sample_data = {
        'list1': [1, 2, 3, 4],
        'list2': ['a', 'b', 'c'],
        'empty_list': [],
        'single_item': [99]
    }
    
    for key, value in sample_data.items():
        print(f"First element of {key}: {get_first_element(value)}")