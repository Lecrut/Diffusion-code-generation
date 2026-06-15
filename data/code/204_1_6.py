def find_middle_value(data):
    n = len(data)
    sorted_data = sorted(data)
    if n % 2 == 1:
        middle_index = n // 2
        return sorted_data[middle_index]
    else:
        mid1_index = n // 2 - 1
        mid2_index = n // 2
        middle1 = sorted_data[mid1_index]
        middle2 = sorted_data[mid2_index]
        return (middle1 + middle2) / 2
if __name__ == '__main__':
    list1 = [1, 3, 2]
    list2 = [1, 5, 2, 4]
    list3 = [1, 2, 3, 4, 5]
    list4 = [10, 20, 30, 40]
    list5 = [7, 1, 5, 3, 9]
    print(f"Median of {list1}: {find_middle_value(list1)}")
    print(f"Median of {list2}: {find_middle_value(list2)}")
    print(f"Median of {list3}: {find_middle_value(list3)}")
    print(f"Median of {list4}: {find_middle_value(list4)}")
    print(f"Median of {list5}: {find_middle_value(list5)}")