def get_penultimate_element(lst):
    if len(lst) < 2:
        raise ValueError("List must contain at least two elements")
    return lst[-2]

if __name__ == '__main__':
    sample_list = [10, 20, 30, 40, 50]
    result = get_penultimate_element(sample_list)
    print(result)

    empty_list = []
    try:
        get_penultimate_element(empty_list)
    except ValueError as e:
        print(str(e))

    single_element_list = [42]
    try:
        get_penultimate_element(single_element_list)
    except ValueError as e:
        print(str(e))

    two_element_list = [1, 2]
    result = get_penultimate_element(two_element_list)
    print(result)