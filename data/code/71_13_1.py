def find_middle_element(data_list):
    n = len(data_list)
    if n == 0:
        raise IndexError("Cannot find the middle element of an empty list.")
    middle_index = n // 2
    return data_list[middle_index]
if __name__ == '__main__':
    list1 = [1, 2, 3, 4, 5]
    list2 = [10, 20, 30, 40]
    list3 = [99]
    list4 = []
    print(f"Middle element of {list1}: {find_middle_element(list1)}")
    print(f"Middle element of {list2}: {find_middle_element(list2)}")
    print(f"Middle element of {list3}: {find_middle_element(list3)}")
    try:
        find_middle_element(list4)
    except IndexError as e:
        print(f"Error for {list4}: {e}")