def get_last_element(lst):
    if not lst:
        raise ValueError("The list is empty")
    return lst[-1]

if __name__ == '__main__':
    sample_list_1 = [1, 2, 3, 4, 5]
    try:
        print(get_last_element(sample_list_1))
    except ValueError as e:
        print(e)

    sample_list_2 = []
    try:
        print(get_last_element(sample_list_2))
    except ValueError as e:
        print(e)

    sample_list_3 = [42, 7, 0]
    try:
        print(get_last_element(sample_list_3))
    except ValueError as e:
        print(e)