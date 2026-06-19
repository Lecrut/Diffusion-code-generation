def get_first_element(data_list):
    if not data_list:
        raise ValueError("The input list is empty.")
    return data_list[0]

if __name__ == '__main__':
    sample_data = [5, 15, 25, 35]
    first_element = get_first_element(sample_data)
    print(first_element)

    try:
        empty_data = []
        first_empty = get_first_element(empty_data)
        print(first_empty)
    except ValueError as e:
        print(e)

    sample_single = [42]
    first_single = get_first_element(sample_single)
    print(first_single)