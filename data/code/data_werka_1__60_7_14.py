def get_last_element(data_list):
    if not data_list:
        raise IndexError("Cannot access the last element from an empty list.")
    return data_list[-1]

if __name__ == '__main__':
    sample_list = [1, 2, 3, 4, 5]
    try:
        print(get_last_element(sample_list))
    except IndexError as e:
        print(e)

    empty_list = []
    try:
        print(get_last_element(empty_list))
    except IndexError as e:
        print(e)