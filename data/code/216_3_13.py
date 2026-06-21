def find_middle(data):
    n = len(data)
    if n == 0:
        return None
    elif n == 1:
        return data[0]
    else:
        middle_index = n // 2
        if n % 2 == 0:
            return (data[middle_index - 1] + data[middle_index]) / 2.0
        else:
            return data[middle_index]

if __name__ == '__main__':
    list1 = [1, 2, 3, 4, 5]
    list2 = [10, 20, 30, 40]
    list3 = [1, 2]
    list4 = [1, 2, 3]
    print(f"Middle of {list1}: {find_middle(list1)}")
    print(f"Middle of {list2}: {find_middle(list2)}")
    print(f"Middle of {list3}: {find_middle(list3)}")
    print(f"Middle of {list4}: {find_middle(list4)}")