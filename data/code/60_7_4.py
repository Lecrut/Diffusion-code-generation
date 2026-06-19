def get_last_element(data_list):
    if not data_list:
        raise IndexError("Cannot retrieve the last element from an empty list.")
    return data_list[-1]

if __name__ == '__main__':
    sample_lists = {
        'list1': [1, 2, 3, 4, 5],
        'list2': [],
        'list3': ['a', 'b', 'c'],
    }
    
    for name, lst in sample_lists.items():
        try:
            result = get_last_element(lst)
            print(f"Result for {name}: {result}")
        except IndexError as e:
            print(f"Error for {name}: {e}")