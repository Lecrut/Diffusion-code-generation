def get_penultimate_element(lst):
    if len(lst) < 2:
        raise ValueError("List must contain at least two elements")
    return lst[-2]

if __name__ == '__main__':
    sample_list = [1, 2, 3, 4, 5]
    result = get_penultimate_element(sample_list)
    print(result)
    
    try:
        empty_list = []
        get_penultimate_element(empty_list)
    except ValueError as e:
        print(e)
    
    try:
        single_element_list = [1]
        get_penultimate_element(single_element_list)
    except ValueError as e:
        print(e)