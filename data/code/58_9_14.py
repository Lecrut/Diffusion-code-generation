def get_first_element(lst):
    if not lst:
        return None
    return lst[0]

if __name__ == '__main__':
    SAMPLE_LIST = [10, 20, 30, 40]
    EMPTY_LIST = []
    
    first_element = get_first_element(SAMPLE_LIST)
    print(first_element)
    
    first_empty = get_first_element(EMPTY_LIST)
    print(first_empty)