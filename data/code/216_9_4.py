def calculate_middle(data):
    n = len(data)
    middle_index = n // 2
    return data[middle_index]
if __name__ == '__main__':
    sorted_list1 = [2, 4, 6, 8, 10]
    sorted_list2 = [1, 5, 9, 13, 17, 21]
    sorted_list3 = [5]
    sorted_list4 = [10, 20, 30]
    print(calculate_middle(sorted_list1))
    print(calculate_middle(sorted_list2))
    print(calculate_middle(sorted_list3))
    print(calculate_middle(sorted_list4))