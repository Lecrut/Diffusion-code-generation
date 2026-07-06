def find_middle_element(data):
    n = len(data)
    middle_index = n // 2
    if n % 2 == 0:
        return data[middle_index - 1]
    else:
        return data[middle_index]
if __name__ == '__main__':
    list1 = [1.0, 2.0, 3.0, 4.0, 5.0]
    list2 = [10.2, 2, 0, 3, 4, 4, 0]
    list3 = []
    list4 = [1, 1,2.0, 3.0, 4, 4.5, 5, 20]
    list5 = [1.0, 2.0]
    print(find_middle_element(list1))
    print(find_middle_element(list2))
    print(find_middle_element(list3))
    print(find_middle_element(list4))
    print(find_middle_element(list5))
