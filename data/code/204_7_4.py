def find_middle(data):
    n = len(data)
    if n == 0:
        return None
    middle_index = n // 2
    return data[middle_index]
if __name__ == '__main__':
    list1 = [1, 2, 3, 4, 5]
    print(find_middle(list1))
    list2 = [10, 20, 30, 40, 50, 60]
    print(find_middle(list2))
    list3 = [7]
    print(find_middle(list3))
    list4 = []
    print(find_middle(list4))