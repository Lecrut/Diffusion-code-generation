MIDDLE_INDEX = lambda n: n // 2

def find_middle_value(lst):
    lst.sort()
    length = len(lst)
    if length % 2 == 0:
        return (lst[MIDDLE_INDEX(length - 1)] + lst[MIDDLE_INDEX(length)]) / 2
    else:
        return lst[MIDDLE_INDEX(length)]

if __name__ == '__main__':
    sample_list = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
    print(find_middle_value(sample_list))