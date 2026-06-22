def safe_second_element(lst):
    if len(lst) < 2:
        return None
    second_element = lst[1]
    return second_element

if __name__ == '__main__':
    sample_list_1 = [100, 200, 300]
    sample_list_2 = ['single']
    sample_list_3 = []
    print(safe_second_element(sample_list_1))
    print(safe_second_element(sample_list_2))
    print(safe_second_element(sample_list_3))