def check_first_and_last(data):
    if not data:
        return None, None
    first_element = data[0]
    last_element = data[-1]
    return first_element, last_element

if __name__ == '__main__':
    sample_list = [7, 8, 9, 10, 11]
    first_value, last_value = check_first_and_last(sample_list)
    print(f"First: {first_value}, Last: {last_value}")
    
    single_element_list = [42]
    first_single, last_single = check_first_and_last(single_element_list)
    print(f"First (single element): {first_single}, Last (single element): {last_single}")
    
    empty_list = []
    first_empty, last_empty = check_first_and_last(empty_list)
    print(f"First (empty list): {first_empty}, Last (empty list): {last_empty}")
    
    another_sample_list = [100, 200, 300]
    first_another, last_another = check_first_and_last(another_sample_list)
    print(f"First: {first_another}, Last: {last_another}")