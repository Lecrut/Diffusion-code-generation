def check_first_and_last(data):
    if not data:
        return None, None
    return data[0], data[-1]

if __name__ == '__main__':
    sample_list = [15, 25, 35, 45, 55]
    first, last = check_first_and_last(sample_list)
    print(f"First: {first}, Last: {last}")
    
    single_element_list = [75]
    first_single, last_single = check_first_and_last(single_element_list)
    print(f"First (single): {first_single}, Last (single): {last_single}")
    
    empty_list = []
    first_empty, last_empty = check_first_and_last(empty_list)
    print(f"First (empty): {first_empty}, Last (empty): {last_empty}")