def find_median(data):
    n = len(data)
    if n == 0:
        return None
    sorted_data = sorted(data)
    if n % 2 == 1:
        middle_index = n // 2
        return sorted_data[middle_index]
    else:
        upper_middle_index = n // 2
        lower_middle_index = upper_middle_index - 1
        median = (sorted_data[lower_middle_index] + sorted_data[upper_middle_index]) / 2
        return median
if __name__ == '__main__':
    list1 = [1, 5, 2, 8, 3]
    list2 = [10, 4, 7, 2, 9]
    list3 = [1, 2, 3, 4, 5, 6]
    list4 = [10, 20, 30]
    list5 = []
    print(f"Median of {list1}: {find_median(list1)}")
    print(f"Median of {list2}: {find_median(list2)}")
    print(f"Median of {list3}: {find_median(list3)}")
    print(f"Median of {list4}: {find_median(list4)}")
    print(f"Median of {list5}: {find_median(list5)}")