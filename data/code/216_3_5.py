def find_middle_element(data):
    n = len(data)
    if n % 2 == 1:
        middle_index = n // 2
        return data[middle_index]
    else:
        middle_right_index = n // 2
        middle_left_index = middle_right_index - 1
        middle_left = data[middle_left_index]
        middle_right = data[middle_right_index]
        return (middle_left + middle_right) / 2
if __name__ == '__main__':
    list1 = [1, 2, 3, 4, 5]
    list2 = [10, 20, 30, 40]
    list3 = [1, 2]
    list4 = [1, 2, 3]
    print(f"Middle element of {list1}: {find_middle_element(list1)}")
    print(f"Middle element of {list2}: {find_middle_element(list2)}")
    print(f"Middle element of {list3}: {find_middle_element(list3)}")
    print(f"Middle element of {list4}: {find_middle_element(list4)}")