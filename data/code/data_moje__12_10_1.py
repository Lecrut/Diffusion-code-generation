def get_middle_element(lst):
    if not lst:
        return None
    return lst[len(lst) // 2]

if __name__ == '__main__':
    sample_list_1 = [1, 2, 3, 4, 5]
    sample_list_2 = [1, 2, 3, 4]
    sample_list_3 = []

    result_1 = get_middle_element(sample_list_1)
    result_2 = get_middle_element(sample_list_2)
    result_3 = get_middle_element(sample_list_3)

    print(result_1)
    print(result_2)
    print(result_3)