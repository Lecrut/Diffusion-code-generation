def is_list_long_enough(lst):
    return len(lst) > 1

def safe_second_element(lst):
    if not is_list_long_enough(lst):
        return None
    return lst[1]

if __name__ == '__main__':
    sample_list_1 = [5, 10, 15]
    sample_list_2 = ['x']
    sample_list_3 = []
    print(safe_second_element(sample_list_1))
    print(safe_second_element(sample_list_2))
    print(safe_second_element(sample_list_3))