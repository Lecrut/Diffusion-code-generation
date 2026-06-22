def get_first_element(lst):
    if not lst:
        raise ValueError("The list is empty")
    return lst[0]

if __name__ == '__main__':
    sample_list = [1, 2, 3, 4, 5]
    try:
        print(get_first_element(sample_list))
    except ValueError as e:
        print(e)

    empty_list = []
    try:
        print(get_first_element(empty_list))
    except ValueError as e:
        print(e)