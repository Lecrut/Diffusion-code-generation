def find_middle_value(lst):
    lst.sort()
    n = len(lst)
    if n % 2 == 0:
        return (lst[n // 2 - 1] + lst[n // 2]) / 2
    else:
        return lst[n // 2]

if __name__ == '__main__':
    sample_list_1 = [7, 3, 5]
    print(find_middle_value(sample_list_1))
    sample_list_2 = [9, 4, 6, 2]
    print(find_middle_value(sample_list_2))