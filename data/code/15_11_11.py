def get_penultimate(lst):
    if len(lst) < 2:
        raise ValueError("List must have at least two elements")
    return lst[-2]

if __name__ == '__main__':
    sample_list = [10, 20, 30, 40, 50]
    print(get_penultimate(sample_list))

    short_list = [5, 15]
    print(get_penultimate(short_list))

    try:
        single_element_list = [42]
        print(get_penultimate(single_element_list))
    except ValueError as e:
        print(e)

    empty_list = []
    try:
        print(get_penultimate(empty_list))
    except ValueError as e:
        print(e)