def check_first_and_last(data):
    if len(data) == 0:
        return None, None
    if len(data) == 1:
        return data[0], data[0]
    return data[0], data[-1]

if __name__ == '__main__':
    sample_list = [15, 25, 35, 45, 55]
    first_val, last_val = check_first_and_last(sample_list)
    print(f"First: {first_val}, Last: {last_val}")
    
    single_element_list = [75]
    first_single, last_single = check_first_and_last(single_element_list)
    print(f"First and Last (single element): {first_single}, {last_single}")
    
    empty_list = []
    first_empty, last_empty = check_first_and_last(empty_list)
    print(f"First: {first_empty}, Last: {last_empty}")