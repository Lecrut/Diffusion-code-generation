def get_middle_element(data):
    n = len(data)
    if n == 0:
        return None
    middle_index = n // 2
    return data[middle_index]
if __name__ == '__main__':
    list1 = [1, 2, 3, 4, 5]
    list2 = [10, 20, 30]
    list3 = [50]
    list4 = []
    list5 = [1, 2, 3, 4]
    list6 = [100, 200]
    print(get_middle_element(list1))
    print(get_middle_element(list2))
    print(get_middle_element(list3))
    print(get_middle_element(list4))
    print(get_middle_element(list5))
    print(get_middle_element(list6))