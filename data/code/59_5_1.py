def find_middle_element(data):
    n = len(data)
    middle_index = n // 2
    if n % 2 == 0:
        return data[middle_index - 1]
    else:
        return data[middle_index]
if __name__ == '__main__':
    list1 = [1.0, 2.0, 3.0, 4.0, 5.0]
    list2 = [10.0, 20.0, 30.0, 40.0]
    list3 = [5.5]
    list4 = [1.0, 2.0, 3.0, 4.0, 5.0, 6.0]
    list5 = [100.0]
    print(find_middle_element(list1))
    print(find_middle_element(list2))
    print(find_middle_element(list3))
    print(find_middle_element(list4))
    print(find_middle_element(list5))