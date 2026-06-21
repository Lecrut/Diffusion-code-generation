def find_middle_value(data):
    n = len(data)
    if n % 2 == 1:
        return data[n // 2]
    else:
        upper_middle_index = n // 2
        lower_middle_index = upper_middle_index - 1
        median = (data[lower_middle_index] + data[upper_middle_index]) / 2.0
        return median

if __name__ == '__main__':
    list1 = [1, 3, 2]
    list2 = [1, 5, 3, 4, 2]
    list3 = [10, 20, 30, 40]
    list4 = [7, 8, 9, 10]
    list5 = [1, 2, 3, 4, 5, 6]
    print(f"Median of {list1}: {find_middle_value(list1)}")
    print(f"Median of {list2}: {find_middle_value(list2)}")
    print(f"Median of {list3}: {find_middle_value(list3)}")
    print(f"Median of {list4}: {find_middle_value(list4)}")
    print(f"Median of {list5}: {find_middle_value(list5)}")