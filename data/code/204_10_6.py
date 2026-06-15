def find_middle_value(data):
    n = len(data)
    sorted_data = sorted(data)
    if n % 2 == 1:
        middle_index = n // 2
        return sorted_data[middle_index]
    else:
        mid1_index = n // 2 - 1
        mid2_index = n // 2
        median = (sorted_data[mid1_index] + sorted_data[mid2_index]) / 2
        return median
if __name__ == '__main__':
    list1 = [1, 3, 2]
    list2 = [1, 5, 3, 7]
    list3 = [10, 20, 30, 40, 50]
    list4 = [1, 2, 3, 4, 5, 6]
    list5 = [1, 2, 3, 4]
    print(f"Median of {list1}: {find_middle_value(list1)}")
    print(f"Median of {list2}: {find_middle_value(list2)}")
    print(f"Median of {list3}: {find_middle_value(list3)}")
    print(f"Median of {list4}: {find_middle_value(list4)}")
    print(f"Median of {list5}: {find_middle_value(list5)}")