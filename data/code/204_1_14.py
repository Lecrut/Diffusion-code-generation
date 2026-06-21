def find_middle_value(data):
    n = len(data)
    if n % 2 == 1:
        return data[n // 2]
    else:
        upper_middle_index = n // 2
        lower_middle_index = upper_middle_index - 1
        return (data[lower_middle_index] + data[upper_middle_index]) / 2

if __name__ == '__main__':
    list1 = [1, 5, 3, 7, 2]
    list2 = [1, 2, 3, 4]
    list3 = [10, 20, 30, 40, 50]
    list4 = [1, 2, 3, 4, 5, 6]
    print(f"Median of {list1}: {find_middle_value(list1)}")
    print(f"Median of {list2}: {find_middle_value(list2)}")
    print(f"Median of {list3}: {find_middle_value(list3)}")
    print(f"Median of {list4}: {find_middle_value(list4)}")