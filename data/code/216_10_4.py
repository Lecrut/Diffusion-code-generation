def calculate_middle_value(data):
    n = len(data)
    if n % 2 == 1:
        middle_index = n // 2
        return data[middle_index]
    else:
        middle_right_index = n // 2
        middle_left_index = middle_right_index - 1
        middle_value = (data[middle_left_index] + data[middle_right_index]) / 2
        return middle_value
if __name__ == '__main__':
    list1 = [1, 2, 3, 4, 5]
    list2 = [10, 20, 30, 40]
    list3 = [1, 2, 3, 4]
    list4 = [5, 10, 15, 20, 25]
    print(f"Middle value of {list1}: {calculate_middle_value(list1)}")
    print(f"Middle value of {list2}: {calculate_middle_value(list2)}")
    print(f"Middle value of {list3}: {calculate_middle_value(list3)}")
    print(f"Middle value of {list4}: {calculate_middle_value(list4)}")