def get_first_element(lst):
    if not lst:
        raise ValueError("The input list is empty")
    return lst[0]

if __name__ == '__main__':
    sample_list = [7, 8, 9, 10, 11]
    try:
        print(get_first_element(sample_list))
    except ValueError as e:
        print(e)
    
    empty_list = []
    try:
        print(get_first_element(empty_list))
    except ValueError as e:
        print(e)
    
    single_element_list = [99]
    try:
        print(get_first_element(single_element_list))
    except ValueError as e:
        print(e)