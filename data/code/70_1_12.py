def check_first_and_last(data):
    if not data:
        return None, None
    first_element = data[0]
    last_element = data[-1]
    return first_element, last_element

if __name__ == '__main__':
    sample_list = [7, 14, 21, 28, 35]
    first, last = check_first_and_last(sample_list)
    print(f"First: {first}, Last: {last}")
    
    single_element_list = [42]
    first_single, last_single = check_first_and_last(single_element_list)
    print(f"Single element First: {first_single}, Single element Last: {last_single}")
    
    empty_list = []
    first_empty, last_empty = check_first_and_last(empty_list)
    print(f"Empty list First: {first_empty}, Empty list Last: {last_empty}")
    
    large_list = [100, 200, 300, 400, 500, 600, 700]
    first_large, last_large = check_first_and_last(large_list)
    print(f"Large list First: {first_large}, Large list Last: {last_large}")