def check_tuple_existence(data_list, target_tuple):
    if not isinstance(data_list, list) or not all(isinstance(item, tuple) for item in data_list):
        raise ValueError("data_list must be a list of tuples")
    if not isinstance(target_tuple, tuple):
        raise ValueError("target_tuple must be a tuple")

    return target_tuple in data_list

if __name__ == '__main__':
    sample_list = [(1, 2), (3, 4), (5, 6)]
    target_1 = (3, 4)
    print(f"List: {sample_list}, Target: {target_1} -> Result: {check_tuple_existence(sample_list, target_1)}")
    
    sample_list_2 = [(7, 8), (9, 10)]
    target_2 = (11, 12)
    print(f"List: {sample_list_2}, Target: {target_2} -> Result: {check_tuple_existence(sample_list_2, target_2)}")