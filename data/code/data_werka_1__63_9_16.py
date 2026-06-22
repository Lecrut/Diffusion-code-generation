def get_first_element(data_list):
    if not data_list:
        raise ValueError("The input list is empty.")
    return data_list[0]

if __name__ == '__main__':
    sample_data = [42, 73, 100]
    first_element = get_first_element(sample_data)
    print(first_element)

    try:
        empty_sample = []
        empty_first_element = get_first_element(empty_sample)
    except ValueError as e:
        print(e)

    single_element_sample = [9001]
    single_element = get_first_element(single_element_sample)
    print(single_element)