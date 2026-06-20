def find_middle_element(data):
    if not isinstance(data, list) or len(data) == 0:
        raise ValueError("Input must be a non-empty list")
    return data[len(data) // 2]

if __name__ == '__main__':
    list1 = [1, 2, 3, 4, 5]
    list2 = [10, 20, 30, 40]
    list3 = [100]
    list4 = [5, 15, 25, 35, 45, 55]
    print(f"Middle element of {list1}: {find_middle_element(list1)}")
    print(f"Middle element of {list2}: {find_middle_element(list2)}")
    print(f"Middle element of {list3}: {find_middle_element(list3)}")
    print(f"Middle element of {list4}: {find_middle_element(list4)}")