def find_middle_value(data):
    sorted_data = sorted(data)
    n = len(sorted_data)
    if n % 2 == 1:
        middle_index = n // 2
        return sorted_data[middle_index]
    else:
        middle_right_index = n // 2
        middle_left_index = middle_right_index - 1
        median = (sorted_data[middle_left_index] + sorted_data[middle_right_index]) / 2
        return median
if __name__ == '__main__':
    list1 = [1, 3, 2]
    list2 = [1, 2, 3, 4]
    list3 = [5, 1, 8, 2, 9]
    list4 = [10, 20, 30, 40, 50, 60]
    print(f"Median of {list1}: {find_middle_value(list1)}")
    print(f"Median of {list2}: {find_middle_value(list2)}")
    print(f"Median of {list3}: {find_middle_value(list3)}")
    print(f"Median of {list4}: {find_middle_value(list4)}")