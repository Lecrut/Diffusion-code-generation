def find_middle_element(lst):
    if not isinstance(lst, list):
        raise TypeError('Input must be a list')
    if len(lst) == 0:
        raise ValueError('List cannot be empty')
    n = len(lst)
    middle_index = n // 2
    return lst[middle_index]
if __name__ == '__main__':
    SAMPLE_LIST_EVEN = [3.1, 4.5, 6.7, 8.9]
    SAMPLE_LIST_ODD = [1.1, 2.2, 3.3, 4.4, 5.5]
    print(find_middle_element(SAMPLE_LIST_EVEN))
    print(find_middle_element(SAMPLE_LIST_ODD))