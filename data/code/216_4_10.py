def calculate_median(data):
    n = len(data)
    if n == 0:
        raise ValueError('The list cannot be empty')
    sorted_data = sorted(data)
    middle_index = n // 2
    if n % 2 != 0:
        return sorted_data[middle_index]
    else:
        return (sorted_data[middle_index - 1] + sorted_data[middle_index]) / 2
if __name__ == '__main__':
    list1 = [3, 1, 4, 1, 5, 9, 2, 6, 5]
    print(calculate_median(list1))