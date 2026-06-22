def get_first_element(lst):
    is_empty = not lst
    if is_empty:
        return None
    first_elem = lst[0]
    return first_elem

if __name__ == '__main__':
    sample_list = [5, 15, 25, 35, 45]
    empty_list = []
    
    result_non_empty = get_first_element(sample_list)
    print(result_non_empty)
    
    result_empty = get_first_element(empty_list)
    print(result_empty)