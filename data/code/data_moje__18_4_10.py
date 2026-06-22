def get_middle_value(lst):
    length = len(lst)
    middle_index = length // 2
    return lst[middle_index]

if __name__ == '__main__':
    print(get_middle_value([10, 20, 30, 40, 50]))
    print(get_middle_value([1, 2, 3]))
    print(get_middle_value([5]))
    print(get_middle_value([10, 20]))