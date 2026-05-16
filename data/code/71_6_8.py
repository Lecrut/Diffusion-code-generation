def find_median(data):
    n = len(data)
    if n == 0:
        return None
    sorted_data = sorted(data)
    if n % 2 == 1:
        middle_index = n // 2
        return sorted_data[middle_index]
    else:
        lower_middle_index = n // 2 - 1
        return sorted_data[lower_middle_index]
if __name__ == '__main__':
    list1 = [1, 5, 2, 8, 3]
    list2 = [10, 20, 30, 40]
    list3 = [7, 1, 5, 2, 8, 3]
    list4 = [1, 2, 3, 4, 5, 6]
    list5 = [1, 2]
    list6 = []
    print(f"Median of {list1}: {find_median(list1)}")
    print(f"Median of {list2}: {find_median(list2)}")
    print(f"Median of {list3}: {find_median(list3)}")
    print(f"Median of {list4}: {find_median(list4)}")
    print(f"Median of {list5}: {find_median(list5)}")
    print(f"Median of {list6}: {find_median(list6)}")