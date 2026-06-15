def find_middle_value(data):
    n = len(data)
    sorted_data = sorted(data)
    if n % 2 == 1:
        middle_index = n // 2
        return sorted_data[middle_index]
    else:
        upper_middle_index = n // 2
        lower_middle_index = upper_middle_index - 1
        median = (sorted_data[lower_middle_index] + sorted_data[upper_middle_index]) / 2.0
        return median
if __name__ == '__main__':
    list1 = [1, 3, 2]
    print(find_middle_value(list1))
    list2 = [1, 5, 3, 4, 2]
    print(find_middle_value(list2))
    list3 = [10, 20, 30, 40]
    print(find_middle_value(list3))
    list4 = [7, 8, 9, 10, 11]
    print(find_middle_value(list4))
    list5 = [5]
    print(find_middle_value(list5))
    list6 = [2, 4]
    print(find_middle_value(list6))