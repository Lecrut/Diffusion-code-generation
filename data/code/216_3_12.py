def middle_value(lst):
    if len(lst) == 0:
        return None
    elif len(lst) == 1:
        return lst[0]
    else:
        sorted_lst = sorted(lst)
        mid_index = len(sorted_lst) // 2
        return sorted_lst[mid_index]

if __name__ == '__main__':
    print(middle_value([3, 1, 4, 1, 5, 9]))
    print(middle_value([]))
    print(middle_value([7]))