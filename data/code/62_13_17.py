def safe_second_element(lst):
    return lst[1] if len(lst) > 1 else None

if __name__ == '__main__':
    sample_list_1 = [100, 200, 300]
    sample_list_2 = [45]
    sample_list_3 = []
    print(safe_second_element(sample_list_1))
    print(safe_second_element(sample_list_2))
    print(safe_second_element(sample_list_3))