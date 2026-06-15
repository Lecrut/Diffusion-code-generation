def find_middle(data):
    n = len(data)
    if n == 0:
        return None
    middle_index = n // 2
    return data[middle_index]
if __name__ == '__main__':
    list1 = [1, 5, 2, 8, 3]
    print(find_middle(list1))
    list2 = [100, 200, 300, 400, 500, 600]
    print(find_middle(list2))
    list3 = [7]
    print(find_middle(list3))
    list4 = []
    print(find_middle(list4))