def check_first_and_last(data):
    if not data:
        return None, None
    return data[0], data[-1]

if __name__ == '__main__':
    sample_list = [10, 20, 30, 40, 50]
    first_val, last_val = check_first_and_last(sample_list)
    print(f"First: {first_val}, Last: {last_val}")
    
    single_element_list = [7]
    first_single, last_single = check_first_and_last(single_element_list)
    print(f"Single element First: {first_single}, Last: {last_single}")
    
    empty_list = []
    first_empty, last_empty = check_first_and_last(empty_list)
    print(f"Empty list First: {first_empty}, Last: {last_empty}")
    
    multi_element_list = [1, 2, 3, 4, 5, 6]
    first_multi, last_multi = check_first_and_last(multi_element_list)
    print(f"Multi element First: {first_multi}, Last: {last_multi}")