MIDDLE_INDEX = lambda n: n // 2

def get_middle_value(data):
    if not data:
        return None
    middle_index = MIDDLE_INDEX(len(data))
    if len(data) % 2 == 1:
        return data[middle_index]
    else:
        return (data[middle_index - 1] + data[middle_index]) / 2

if __name__ == '__main__':
    list1 = [1, 2, 3, 4, 5]
    print(get_middle_value(list1))
    list2 = [10, 20, 30]
    print(get_middle_value(list2))
    list3 = [7]
    print(get_middle_value(list3))
    list4 = [1, 2, 3, 4]
    print(get_middle_value(list4))