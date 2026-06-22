def get_last_element_safe(data_list):
    if not isinstance(data_list, list):
        raise TypeError("Input must be a list.")
    if len(data_list) == 0:
        raise IndexError("Cannot get the last element from an empty list.")
    return data_list[-1]

if __name__ == '__main__':
    sample_list1 = [1, 2, 3, 4, 5]
    sample_list2 = []
    try:
        print(get_last_element_safe(sample_list1))
    except (TypeError, IndexError) as e:
        print(e)
    try:
        print(get_last_element_safe(sample_list2))
    except (TypeError, IndexError) as e:
        print(e)