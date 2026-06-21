def middle_value(lst):
    length = len(lst)
    if length == 0:
        return None
    elif length == 1:
        return lst[0]
    else:
        mid = length // 2
        return (lst[mid - 1] + lst[mid]) / 2
if __name__ == '__main__':
    print(middle_value([1, 2, 3, 4, 5]))
    print(middle_value([1, 2, 3, 4]))
    print(middle_value([]))
    print(middle_value([42]))