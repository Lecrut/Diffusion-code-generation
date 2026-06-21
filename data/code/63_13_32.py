def get_first_element(lst):
    def is_valid_list(input_value):
        return isinstance(input_value, list)
    
    if not is_valid_list(lst):
        raise ValueError("Input must be a list")
    
    if len(lst) == 0:
        return None
    
    return lst[0]

if __name__ == '__main__':
    sample_data = [
        [10, 20, 30],
        [],
        ["hello", "world"],
        [True, False, True],
        [None, None]
    ]
    
    for data in sample_data:
        print(get_first_element(data))