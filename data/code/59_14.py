def find_middle(data):
    middle_index = len(data) // 2
    return data[middle_index]
if __name__ == '__main__':
    list1 = [1, 2, 3, 4, 5]
    list2 = [10, 20, 30, 40]
    list3 = [50]
    list4 = [100, 200]
    print(find_middle(list1))
    print(find_middle(list2))
    print(find_middle(list3))
    print(find_middle(list4))