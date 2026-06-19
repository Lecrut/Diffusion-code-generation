def safe_second_element(lst):
    try:
        return lst[1]
    except IndexError:
        return None
if __name__ == '__main__':
    sample_list_1 = [1, 2, 3, 4]
    sample_list_2 = [5]
    sample_list_3 = []
    print(safe_second_element(sample_list_1))
    print(safe_second_element(sample_list_2))
    print(safe_second_element(sample_list_3))