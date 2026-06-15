def find_middle_value(data):
    n = len(data)
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
    list1 = [1, 5, 3, 7, 2]
    list2 = [1, 2, 3, 4]
    list3 = [10, 20, 30, 40, 50]
    list4 = [1, 2, 3, 4, 5, 6]
    print(f"List: {list1}, Median: {find_middle_value(list1)}")
    print(f"List: {list2}, Median: {find_middle_value(list2)}")
    print(f"List: {list3}, Median: {find_middle_value(list3)}")
    print(f"List: {list4}, Median: {find_middle_value(list4)}")