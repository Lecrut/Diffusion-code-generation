def find_middle_item(data):
    n = len(data)
    middle_index = (n - 1) // 2
    return data[middle_index]
if __name__ == '__main__':
    list1 = [1, 2, 3, 4, 5]
    list2 = [10, 20, 30, 40]
    list3 = [100]
    list4 = [5, 15, 25, 35, 45, 55]
    print(f"Middle item of {list1}: {find_middle_item(list1)}")
    print(f"Middle item of {list2}: {find_middle_item(list2)}")
    print(f"Middle item of {list3}: {find_middle_item(list3)}")
    print(f"Middle item of {list4}: {find_middle_item(list4)}")