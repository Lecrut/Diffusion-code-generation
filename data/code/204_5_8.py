def get_middle_value(lst):
    lst.sort()
    n = len(lst)
    return lst[n // 2]

if __name__ == '__main__':
    sample_list = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
    print(get_middle_value(sample_list))