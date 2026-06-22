def calculate_median(data):
    if not data:
        raise ValueError('Input list cannot be empty')
    sorted_data = sorted(data)
    n = len(sorted_data)
    mid = n // 2
    if n % 2 == 1:
        return sorted_data[mid]
    else:
        return (sorted_data[mid - 1] + sorted_data[mid]) / 2.0
if __name__ == '__main__':
    list1 = [5, 2, 8, 1, 9]
    list2 = [3, 7, 1, 4, 6, 2]
    median1 = calculate_median(list1)
    median2 = calculate_median(list2)
    print(median1)
    print(median2)