def get_middle_value(lst):
    lst.sort()
    length = len(lst)
    middle_index = length // 2
    if length % 2 == 0:
        return (lst[middle_index - 1] + lst[middle_index]) / 2
    else:
        return lst[middle_index]

if __name__ == '__main__':
    sample_list = [5, 3, 8, 6, 7, 2]
    print(get_middle_value(sample_list))