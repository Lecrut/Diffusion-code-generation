def calculate_median(data):
    n = len(data)
    if n == 0:
        return None
    data.sort()
    middle_index = n // 2
    if n % 2 != 0:
        return data[middle_index]
    else:
        return (data[middle_index - 1] + data[middle_index]) / 2
if __name__ == '__main__':
    list1 = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
    print(calculate_median(list1))
    list2 = []
    print(calculate_median(list2))