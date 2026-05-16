def find_last_index(data, value):
    last_index = -1
    for i in range(len(data) - 1, -1, -1):
        if data[i] == value:
            last_index = i
            break
    return last_index
if __name__ == '__main__':
    list1 = [1, 2, 3, 2, 4, 2]
    value1 = 2
    print(find_last_index(list1, value1))
    list2 = [10, 20, 30, 20, 40]
    value2 = 20
    print(find_last_index(list2, value2))
    list3 = [5, 5, 5, 5]
    value3 = 5
    print(find_last_index(list3, value3))
    list4 = [1, 2, 3, 4]
    value4 = 99
    print(find_last_index(list4, value4))
    list5 = []
    value5 = 1
    print(find_last_index(list5, value5))