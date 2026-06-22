def extract_third_element(lst, default_value=None):
    if len(lst) >= 3:
        return lst[2]
    return default_value

if __name__ == '__main__':
    sample_list_1 = [1, 2, 3, 4, 5]
    sample_list_2 = [1, 2]
    sample_list_3 = []

    result_1 = extract_third_element(sample_list_1, None)
    result_2 = extract_third_element(sample_list_2, 'default')
    result_3 = extract_third_element(sample_list_3, 'empty_default')

    print(result_1)
    print(result_2)
    print(result_3)