def get_last_element(data_list):
    if not data_list:
        raise IndexError("Cannot access the last element from an empty list.")
    return data_list[-1]

if __name__ == '__main__':
    sample_lists = [
        [1, 2, 3, 4, 5],
        [],
        ['a', 'b', 'c'],
        [True, False]
    ]
    
    for i, lst in enumerate(sample_lists):
        try:
            print(f"Last element of list {i+1}: {get_last_element(lst)}")
        except IndexError as e:
            print(f"Error for list {i+1}: {e}")