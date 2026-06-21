def get_first_element(lst):
    if not lst:
        raise ValueError("The input list is empty")
    return lst[0]

if __name__ == '__main__':
    try:
        sample_list = [1, 2, 3, 4, 5]
        print(get_first_element(sample_list))
    except ValueError as e:
        print(e)
    
    try:
        empty_list = []
        print(get_first_element(empty_list))
    except ValueError as e:
        print(e)
    
    try:
        single_element_list = [42]
        print(get_first_element(single_element_list))
    except ValueError as e:
        print(e)