def safe_second_element(lst):
    return lst[1] if len(lst) > 1 else None
if __name__ == '__main__':
    sample_list_1 = [1, 2, 3]
    sample_list_2 = [42]
    sample_list_3 = []
    print(safe_second_element(sample_list_1))
    print(safe_second_element(sample_list_2))
    print(safe_second_element(sample_list_3))