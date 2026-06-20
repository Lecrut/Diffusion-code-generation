def find_middle_element(data):
    n = len(data)
    if n % 2 == 1:
        return data[n // 2]
    else:
        raise ValueError("List has an even number of elements")

if __name__ == '__main__':
    list1 = [1, 2, 3, 4, 5]
    list2 = [10, 20, 30, 40]
    list3 = [100]
    list4 = [5, 15, 25, 35, 45, 55]
    try:
        print(find_middle_element(list1))
        print(find_middle_element(list2))
        print(find_middle_element(list3))
        print(find_middle_element(list4))
    except ValueError as e:
        print(e)