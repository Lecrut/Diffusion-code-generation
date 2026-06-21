def get_first_element(lst):
    if len(lst) == 0:
        raise ValueError("The input list is empty")
    return lst[0]

if __name__ == '__main__':
    SAMPLE_LIST = [1, 2, 3, 4, 5]
    EMPTY_LIST = []
    SINGLE_ELEMENT_LIST = [42]
    
    try:
        print(get_first_element(SAMPLE_LIST))
    except ValueError as e:
        print(e)
    
    try:
        print(get_first_element(EMPTY_LIST))
    except ValueError as e:
        print(e)
    
    try:
        print(get_first_element(SINGLE_ELEMENT_LIST))
    except ValueError as e:
        print(e)