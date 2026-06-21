def middle_value(lst):
    n = len(lst)
    if n == 0:
        return None
    elif n == 1:
        return lst[0]
    else:
        mid = n // 2
        return (lst[mid - 1] + lst[mid]) / 2
if __name__ == '__main__':
    print(middle_value([1, 3, 5]))
    print(middle_value([1, 2, 3, 4]))
    print(middle_value([]))
    print(middle_value([7]))