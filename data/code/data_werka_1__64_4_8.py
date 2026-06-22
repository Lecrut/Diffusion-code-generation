def find_last_index(data, value):
    try:
        return data[::-1].index(value) + len(data) - 1
    except ValueError:
        return -1
if __name__ == '__main__':
    list1 = [3, 5, 2, 5, 8, 5]
    value1 = 5
    print(find_last_index(list1, value1))
    list2 = [10, 20, 30, 20, 40]
    value2 = 20
    print(find_last_index(list2, value2))
    list3 = [1, 2, 3, 4, 5]
    value3 = 99
    print(find_last_index(list3, value3))
    list4 = [7, 8, 9, 8, 7]
    value4 = 8
    print(find_last_index(list4, value4))