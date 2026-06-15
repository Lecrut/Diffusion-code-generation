def find_median(data):
    n = len(data)
    if n == 0:
        return None
    sorted_data = sorted(data)
    if n % 2 == 1:
        middle_index = n // 2
        median = sorted_data[middle_index]
    else:
        upper_middle_index = n // 2
        lower_middle_index = upper_middle_index - 1
        median = (sorted_data[lower_middle_index] + sorted_data[upper_middle_index]) / 2.0
    return median
if __name__ == '__main__':
    list1 = [5, 2, 8, 1, 9]
    print(find_median(list1))
    list2 = [3, 1, 4, 1, 5, 9, 2, 6, 5]
    print(find_median(list2))
    list3 = [10, 20, 30, 40]
    print(find_median(list3))
    list4 = [7]
    print(find_median(list4))
    list5 = []
    print(find_median(list5))