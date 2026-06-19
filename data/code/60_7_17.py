def get_last_element(data_list):
    if not data_list:
        raise IndexError("Cannot access the last element from an empty list.")
    return data_list[-1]

if __name__ == '__main__':
    example_list = [10, 20, 30, 40, 50]
    try:
        last_element = get_last_element(example_list)
        print(f"The last element is: {last_element}")
    except IndexError as e:
        print(e)

    empty_list = []
    try:
        last_element_empty = get_last_element(empty_list)
        print(f"The last element is: {last_element_empty}")
    except IndexError as e:
        print(e)