def get_first_element(lst):
    if not lst:
        raise IndexError("The list is empty")
    return lst[0]

if __name__ == '__main__':
    sample_list = [5, 15, 25, 35]
    try:
        print(get_first_element(sample_list))
    except IndexError as e:
        print(e)

    empty_list = []
    try:
        print(get_first_element(empty_list))
    except IndexError as e:
        print(e)