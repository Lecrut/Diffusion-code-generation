def get_first_element(lst):
    if not lst:
        raise ValueError("The input list is empty")
    return lst[0]

if __name__ == '__main__':
    try:
        sample_list = [100, 200, 300]
        first_element = get_first_element(sample_list)
        print(f"The first element of the sample list is: {first_element}")
    except ValueError as e:
        print(e)

    empty_list = []
    try:
        first_element = get_first_element(empty_list)
        print(f"The first element of the empty list is: {first_element}")
    except ValueError as e:
        print(e)

    single_element_list = [42]
    try:
        first_element = get_first_element(single_element_list)
        print(f"The first element of the single-element list is: {first_element}")
    except ValueError as e:
        print(e)