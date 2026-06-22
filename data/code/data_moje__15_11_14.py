def get_penultimate(lst):
    if len(lst) < 2:
        raise ValueError("List must have at least two elements")
    return lst[-2]

if __name__ == '__main__':
    sample_list = [10, 20, 30, 40, 50]
    result = get_penultimate(sample_list)
    print(result)

    small_list = [7, 8]
    result2 = get_penultimate(small_list)
    print(result2)

    try:
        single_element = [42]
        get_penultimate(single_element)
    except ValueError as e:
        print(str(e))

    try:
        empty_list = []
        get_penultimate(empty_list)
    except ValueError as e:
        print(str(e))