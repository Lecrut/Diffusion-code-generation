def get_first_element(data):
    if not data:
        raise IndexError("list is empty")
    return data[0]

if __name__ == '__main__':
    sample_data = {
        'list1': [1, 2, 3, 4],
        'list2': ['a', 'b', 'c'],
        'empty_list': []
    }
    
    for key, value in sample_data.items():
        try:
            print(f"First element of {key}: {get_first_element(value)}")
        except IndexError as e:
            print(f"Error caught for {key}: {e}")