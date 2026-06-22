def get_penultimate_element(lst):
    if len(lst) < 2:
        raise ValueError("List must have at least two elements to get the penultimate element")
    return lst[-2]

if __name__ == '__main__':
    sample_list = [1, 2, 3, 4, 5]
    result = get_penultimate_element(sample_list)
    print(result)

    another_list = ['a', 'b', 'c']
    result2 = get_penultimate_element(another_list)
    print(result2)

    try:
        empty_list = []
        get_penultimate_element(empty_list)
    except ValueError as e:
        print(e)

    single_element_list = [42]
    try:
        get_penultimate_element(single_element_list)
    except ValueError as e:
        print(e)