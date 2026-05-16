def find_middle(data):
    n = len(data)
    if n == 0:
        return None
    if n % 2 == 1:
        middle_index = n // 2
        return data[middle_index]
    else:
        middle_right_index = n // 2
        middle_left_index = middle_right_index - 1
        return (data[middle_left_index] + data[middle_right_index]) / 2
if __name__ == '__main__':
    list1 = [1, 2, 3, 4, 5]
    list2 = [10, 20, 30, 40, 50, 60]
    list3 = [1, 2, 3, 4]
    list4 = []
    list5 = [5.5, 6.5]
    print(f"Middle of {list1}: {find_middle(list1)}")
    print(f"Middle of {list2}: {find_middle(list2)}")
    print(f"Middle of {list3}: {find_middle(list3)}")
    print(f"Middle of {list4}: {find_middle(list4)}")
    print(f"Middle of {list5}: {find_middle(list5)}")