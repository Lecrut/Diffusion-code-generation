def compare_first_two_elements(lst):
    return lst[0] > lst[1]
if __name__ == '__main__':
    SAMPLE_LIST_1 = [5, 3]
    SAMPLE_LIST_2 = [10, 15]
    SAMPLE_LIST_3 = [7.8, 7.8]
    print(compare_first_two_elements(SAMPLE_LIST_1))
    print(compare_first_two_elements(SAMPLE_LIST_2))
    print(compare_first_two_elements(SAMPLE_LIST_3))