def get_last_element(lst):
    if not lst:
        raise IndexError("Cannot get the last element from an empty list.")
    return lst[-1]

if __name__ == '__main__':
    test_list = [100, 200, 300, 400, 500]
    try:
        last_element = get_last_element(test_list)
        print(f"The last element of the list is: {last_element}")
    except IndexError as e:
        print(e)

    empty_list = []
    try:
        last_element_empty = get_last_element(empty_list)
        print(f"The last element of the empty list is: {last_element_empty}")
    except IndexError as e:
        print(e)