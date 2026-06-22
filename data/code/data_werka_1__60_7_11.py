def is_list_empty(data_list):
    return len(data_list) == 0

def get_last_element_safe(data_list):
    if is_list_empty(data_list):
        raise IndexError("Cannot retrieve the last element from an empty list.")
    return data_list[-1]

if __name__ == '__main__':
    test_lists = [
        [1, 2, 3, 4, 5],
        [],
        ['a', 'b', 'c'],
        [True, False]
    ]
    
    for i, lst in enumerate(test_lists):
        try:
            result = get_last_element_safe(lst)
            print(f"Result for list {i+1}: {result}")
        except IndexError as e:
            print(f"Error for list {i+1}: {e}")