def find_middle_element(lst):
    n = len(lst)
    if n == 0:
        return None
    middle_index = n // 2
    return lst[middle_index]
if __name__ == '__main__':
    sample1 = [1, 2, 3, 4, 5]
    print(find_middle_element(sample1))
    sample2 = [10, 20, 30]
    print(find_middle_element(sample2))
    sample3 = [7]
    print(find_middle_element(sample3))