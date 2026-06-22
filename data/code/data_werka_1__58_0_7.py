def get_first_element_safely(data_list):
    if not data_list:
        raise ValueError("The list is empty.")
    return data_list[0]

if __name__ == '__main__':
    try:
        sample_list = [1, 2, 3, 4]
        first_element = get_first_element_safely(sample_list)
        print(first_element)
    except ValueError as e:
        print(e)