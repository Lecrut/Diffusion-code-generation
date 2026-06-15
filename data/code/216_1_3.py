def find_middle(data):
    n = len(data)
    middle_index = n // 2
    return data[middle_index]
if __name__ == '__main__':
    list1 = [1, 2, 3, 4, 5]
    list2 = [10, 20, 30, 40, 50, 60]
    list3 = [7]
    list4 = [99, 88]
    print(find_middle(list1))
    print(find_middle(list2))
    print(find_middle(list3))
    print(find_middle(list4))