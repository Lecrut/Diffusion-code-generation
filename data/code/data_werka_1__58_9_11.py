def get_first_element(lst):
    if not lst:
        raise IndexError("The list is empty")
    return lst[0]

if __name__ == '__main__':
    sample_list = [5, 15, 25, 35]
    try:
        first_element = get_first_element(sample_list)
        print(first_element)
    except IndexError as e:
        print(e)

    empty_list = []
    try:
        first_empty = get_first_element(empty_list)
        print(first_empty)
    except IndexError as e:
        print(e)