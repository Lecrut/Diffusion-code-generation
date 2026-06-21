def get_middle_value(data):
    if not data:
        return None
    mid_index = len(data) // 2
    return data[mid_index]

if __name__ == '__main__':
    list1 = [1, 3, 5, 7, 9]
    list2 = [10, 20, 30, 40]
    list3 = [42]
    list4 = []
    list5 = [100, 200, 300, 400, 500, 600, 700]
    print(get_middle_value(list1))
    print(get_middle_value(list2))
    print(get_middle_value(list3))
    print(get_middle_value(list4))
    print(get_middle_value(list5))