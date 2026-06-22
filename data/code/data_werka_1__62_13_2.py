def safe_second_element(lst):
    if len(lst) < 2:
        return None
    return lst[1]

if __name__ == '__main__':
    sample_list_1 = [10, 20, 30]
    sample_list_2 = [5]
    sample_list_3 = []
    print(safe_second_element(sample_list_1))
    print(safe_second_element(sample_list_2))
    print(safe_second_element(sample_list_3))