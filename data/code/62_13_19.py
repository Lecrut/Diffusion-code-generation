MIN_LIST_LENGTH = 2

def safe_second_element(lst):
    return lst[1] if len(lst) >= MIN_LIST_LENGTH else None

if __name__ == '__main__':
    sample_list_1 = [3, 6, 9]
    sample_list_2 = [45]
    sample_list_3 = []
    print(safe_second_element(sample_list_1))
    print(safe_second_element(sample_list_2))
    print(safe_second_element(sample_list_3))