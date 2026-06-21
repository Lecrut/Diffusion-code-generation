def find_middle_element(lst):
    if not lst:
        raise ValueError('The list is empty')
    MIDDLE_INDEX = len(lst) // 2
    return lst[MIDDLE_INDEX]

if __name__ == '__main__':
    SAMPLE_ODD_LIST = [7, 14, 21, 28, 35]
    SAMPLE_EVEN_LIST = [9, 18, 27, 36, 45, 54]
    print(find_middle_element(SAMPLE_ODD_LIST))
    print(find_middle_element(SAMPLE_EVEN_LIST))