def get_first_element(lst):
    if not lst:
        raise ValueError("The input list is empty")
    first_element = lst[0]
    return first_element

if __name__ == '__main__':
    sample_list = [100, 200, 300, 400, 500]
    try:
        result = get_first_element(sample_list)
        print(result)
    except ValueError as e:
        print(e)
    
    empty_list = []
    try:
        result = get_first_element(empty_list)
        print(result)
    except ValueError as e:
        print(e)
    
    single_element_list = [77]
    try:
        result = get_first_element(single_element_list)
        print(result)
    except ValueError as e:
        print(e)