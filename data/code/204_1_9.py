def find_middle_value(data):
    n = len(data)
    if n == 0:
        raise ValueError("Input list is empty")
    middle_index = n // 2
    return data[middle_index]

if __name__ == '__main__':
    list1 = [1, 5, 3, 7, 2]
    list2 = [1, 2, 3, 4]
    list3 = [10, 20, 30, 40, 50]
    list4 = [1, 2, 3, 4, 5, 6]

    print(f"Median of {list1}: {find_middle_value(list1)}")
    print(f"Median of {list2}: {find_middle_value(list2)}")
    print(f"Median of {list3}: {find_middle_value(list3)}")
    print(f"Median of {list4}: {find_middle_value(list4)}")