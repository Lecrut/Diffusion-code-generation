def find_middle(data):
    n = len(data)
    if n % 2 == 0:
        middle_index = n // 2 - 1
    else:
        middle_index = n // 2
    return data[middle_index]
if __name__ == '__main__':
    list1 = [1, 2, 3, 4]
    list2 = [1, 2, 3, 4, 5]
    list3 = [10, 20]
    list4 = [5]
    print(find_middle(list1))
    print(find_middle(list2))
    print(find_middle(list3))
    print(find_middle(list4))