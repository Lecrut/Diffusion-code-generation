def tuple_exists_in_list(tuple_to_check, list_of_tuples):
    return tuple_to_check in list_of_tuples

if __name__ == '__main__':
    sample_tuple = (3, 4)
    sample_list = [(1, 2), (3, 4), (5, 6)]
    
    if tuple_exists_in_list(sample_tuple, sample_list):
        print(f"The tuple {sample_tuple} exists in the list.")
    else:
        print(f"The tuple {sample_tuple} does not exist in the list.")