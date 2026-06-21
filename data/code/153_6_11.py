def check_tuple_exists(target_tuple, tuple_list):
    if not isinstance(target_tuple, tuple):
        raise ValueError("target_tuple must be a tuple")
    if not all(isinstance(item, tuple) for item in tuple_list):
        raise ValueError("all items in tuple_list must be tuples")
    return target_tuple in tuple_list

if __name__ == '__main__':
    sample_tuple = (1, 2)
    sample_tuple_list = [(3, 4), (5, 6), (1, 2), (7, 8)]
    
    if check_tuple_exists(sample_tuple, sample_tuple_list):
        print(f"'{sample_tuple}' found in the list.")
    else:
        print(f"'{sample_tuple}' not found in the list.")