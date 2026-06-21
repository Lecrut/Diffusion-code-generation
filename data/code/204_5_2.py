def find_middle_value(lst):
    lst.sort()
    length = len(lst)
    if length % 2 == 0:
        return (lst[length // 2 - 1] + lst[length // 2]) / 2
    else:
        return lst[length // 2]

if __name__ == '__main__':
    sample_list = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
    print(find_middle_value(sample_list))