MIDDLE_INDEX = lambda n: n // 2

def find_middle_element(data):
    return data[MIDDLE_INDEX(len(data))]

if __name__ == '__main__':
    list1 = [1, 2, 3, 4, 5]
    list2 = [10, 20, 30]
    list3 = [7]
    list4 = [100, 200, 300, 400, 500, 600]
    print(find_middle_element(list1))
    print(find_middle_element(list2))
    print(find_middle_element(list3))
    print(find_middle_element(list4))