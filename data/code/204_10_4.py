def find_middle_value(data):
    sorted_data = sorted(data)
    n = len(sorted_data)
    if n % 2 == 1:
        middle_index = n // 2
        return sorted_data[middle_index]
    else:
        upper_middle_index = n // 2
        lower_middle_index = upper_middle_index - 1
        middle1 = sorted_data[lower_middle_index]
        middle2 = sorted_data[upper_middle_index]
        return (middle1 + middle2) / 2
if __name__ == '__main__':
    list1 = [1, 3, 2]
    print(find_middle_value(list1))
    list2 = [1, 5, 3, 4, 2]
    print(find_middle_value(list2))
    list3 = [10, 20, 30, 40, 50]
    print(find_middle_value(list3))
    list4 = [1, 2, 3, 4]
    print(find_middle_value(list4))
    list5 = [7, 1, 8, 2, 9, 3]
    print(find_middle_value(list5))