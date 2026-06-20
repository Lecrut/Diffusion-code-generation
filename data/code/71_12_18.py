MIDDLE_INDEX = lambda n: n // 2

def get_middle_value(data):
    n = len(data)
    if n == 0:
        return None
    middle_index = MIDDLE_INDEX(n)
    if n % 2 == 1:
        return data[middle_index]
    else:
        return (data[MIDDLE_INDEX(n - 1)] + data[middle_index]) / 2

if __name__ == '__main__':
    list1 = [1, 2, 3, 4, 5]
    print(get_middle_value(list1))
    list2 = [10, 20, 30, 40, 50, 60]
    print(get_middle_value(list2))
    list3 = [1, 2, 3, 4]
    print(get_middle_value(list3))