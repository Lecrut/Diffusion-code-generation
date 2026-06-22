def get_first_element(lst):
    if not lst:
        return None
    return lst[0]

if __name__ == '__main__':
    SAMPLE_LIST = [1, 2, 3, 4, 5]
    EMPTY_LIST = []
    
    first_element = get_first_element(SAMPLE_LIST)
    print(first_element)
    
    empty_result = get_first_element(EMPTY_LIST)
    print(empty_result)