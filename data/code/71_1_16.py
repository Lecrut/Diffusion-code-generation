def find_middle_element(data):
    n = len(data)
    if n == 0:
        raise ValueError('List is empty')
    middle_index = (n - 1) // 2
    return data[middle_index]
if __name__ == '__main__':
    list1 = [1, 2, 3, 4, 5, 6]
    list2 = [10, 20, 30, 40, 50]
    list3 = [100, 200, 300]
    list4 = [5, 15, 25, 35, 45, 55, 65]
    print(find_middle_element(list1))
    print(find_middle_element(list2))
    print(find_middle_element(list3))
    print(find_middle_element(list4))