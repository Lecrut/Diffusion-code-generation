def get_middle_element(lst):
    if not lst:
        return None
    mid_index = len(lst) // 2
    return lst[mid_index]

if __name__ == '__main__':
    sample1 = [1, 2, 3, 4, 5]
    sample2 = [10, 20, 30, 40]
    sample3 = [7]
    sample4 = []
    print(get_middle_element(sample1))
    print(get_middle_element(sample2))
    print(get_middle_element(sample3))
    print(get_middle_element(sample4))