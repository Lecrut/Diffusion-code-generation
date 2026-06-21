def find_middle(data):
    n = len(data)
    if n == 0:
        return None
    elif n % 2 == 1:
        middle_index = n // 2
        return data[middle_index]
    else:
        middle_right_index = n // 2
        middle_left_index = middle_right_index - 1
        middle_value = (data[middle_left_index] + data[middle_right_index]) / 2.0
        return middle_value

if __name__ == '__main__':
    list1 = [5, 3, 8, 1, 4]
    list2 = [7, 9, 2]
    list3 = []
    list4 = [6]
    
    print(f"Middle of {list1}: {find_middle(list1)}")
    print(f"Middle of {list2}: {find_middle(list2)}")
    print(f"Middle of {list3}: {find_middle(list3)}")
    print(f"Middle of {list4}: {find_middle(list4)}")