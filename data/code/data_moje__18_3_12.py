def get_center_element(lst):
    if not lst:
        raise IndexError("List is empty")
    mid_index = len(lst) // 2
    return lst[mid_index]

if __name__ == '__main__':
    sample1 = [1, 2, 3, 4, 5]
    print(get_center_element(sample1))
    sample2 = [10, 20, 30, 40]
    print(get_center_element(sample2))
    sample3 = [7]
    print(get_center_element(sample3))