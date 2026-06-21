def get_middle_element(lst):
    if not lst:
        return None
    if len(lst) % 2 == 1:
        return lst[len(lst) // 2]
    else:
        return (lst[len(lst) // 2 - 1], lst[len(lst) // 2])

if __name__ == '__main__':
    sample1 = [1, 2, 3, 4, 5]
    sample2 = [1, 2, 3, 4]
    sample3 = [42]
    sample4 = []
    print(get_middle_element(sample1))
    print(get_middle_element(sample2))
    print(get_middle_element(sample3))
    print(get_middle_element(sample4))