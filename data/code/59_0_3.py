def find_middle_item(data):
    n = len(data)
    middle_index = (n - 1) // 2
    return data[middle_index]
if __name__ == '__main__':
    list1 = [1, 2, 3, 4, 5]
    list2 = [10, 20, 30, 40]
    list3 = [50]
    list4 = [100, 200, 300, 400, 500]
    list5 = [1, 2, 3, 4]
    print(find_middle_item(list1))
    print(find_middle_item(list2))
    print(find_middle_item(list3))
    print(find_middle_item(list4))
    print(find_middle_item(list5))