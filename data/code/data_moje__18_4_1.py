def middle_value(lst):
    if not lst:
        return None
    mid_index = len(lst) // 2
    return lst[mid_index]

if __name__ == '__main__':
    print(middle_value([1, 2, 3, 4, 5]))
    print(middle_value([10, 20, 30]))
    print(middle_value([42]))
    print(middle_value([1, 2, 3, 4]))
    print(middle_value([]))