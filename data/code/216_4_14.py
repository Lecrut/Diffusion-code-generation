def calculate_median(data):
    if not data:
        raise ValueError('The input list is empty.')
    sorted_data = sorted(data)
    n = len(sorted_data)
    middle_index = n // 2
    if n % 2 != 0:
        return sorted_data[middle_index]
    else:
        return (sorted_data[middle_index - 1] + sorted_data[middle_index]) / 2
if __name__ == '__main__':
    list1 = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
    list2 = [1, 300, 2, 200, 3]
    list3 = []
    print(calculate_median(list1))
    print(calculate_median(list2))
    try:
        print(calculate_median(list3))
    except ValueError as e:
        print(e)