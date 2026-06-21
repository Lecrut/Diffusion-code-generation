def get_first_element(lst):
    if not lst:
        raise ValueError("The input list is empty")
    return lst[0]

if __name__ == '__main__':
    sample_list = [100, 200, 300, 400, 500]
    try:
        print(get_first_element(sample_list))
    except ValueError as e:
        print(e)

    empty_list = []
    try:
        print(get_first_element(empty_list))
    except ValueError as e:
        print(e)

    single_element_list = [999]
    try:
        print(get_first_element(single_element_list))
    except ValueError as e:
        print(e)