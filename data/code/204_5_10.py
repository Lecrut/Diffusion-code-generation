def find_middle_value(lst):
    lst.sort()
    n = len(lst)
    if n % 2 == 0:
        return (lst[n // 2 - 1] + lst[n // 2]) / 2
    else:
        return lst[n // 2]

if __name__ == '__main__':
    sample_list1 = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
    print(find_middle_value(sample_list1))
    sample_list2 = [10, 20, 30, 40]
    print(find_middle_value(sample_list2))
    sample_list3 = [1]
    print(find_middle_value(sample_list3))