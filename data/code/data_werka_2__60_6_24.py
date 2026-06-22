def get_last_element(lst):
    if not isinstance(lst, list):
        raise TypeError("Input must be a list")
    if len(lst) == 0:
        raise ValueError("List is empty")
    return lst[-1]

if __name__ == '__main__':
    sample_list = [1, 2, 3, 4, 5]
    try:
        print(get_last_element(sample_list))
    except Exception as e:
        print(e)

    empty_list = []
    try:
        print(get_last_element(empty_list))
    except Exception as e:
        print(e)

    non_list_input = "not a list"
    try:
        print(get_last_element(non_list_input))
    except Exception as e:
        print(e)