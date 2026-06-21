def check_first_and_last(data):
    if not data:
        return None, None
    first = data[0]
    last = data[-1]
    return first, last

if __name__ == '__main__':
    SAMPLE_LIST = [15, 25, 35, 45, 55]
    first_val, last_val = check_first_and_last(SAMPLE_LIST)
    print(f"First: {first_val}, Last: {last_val}")
    
    SINGLE_ELEMENT_LIST = [75]
    first_single, last_single = check_first_and_last(SINGLE_ELEMENT_LIST)
    print(f"First (single): {first_single}, Last (single): {last_single}")
    
    EMPTY_LIST = []
    first_empty, last_empty = check_first_and_last(EMPTY_LIST)
    print(f"First (empty): {first_empty}, Last (empty): {last_empty}")
    
    ANOTHER_SAMPLE_LIST = [95]
    first_another, last_another = check_first_and_last(ANOTHER_SAMPLE_LIST)
    print(f"First (another single): {first_another}, Last (another single): {last_another}")