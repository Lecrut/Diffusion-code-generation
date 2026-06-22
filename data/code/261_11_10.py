def calculate_median(data):
    n = len(data)
    if n == 0:
        return None
    sorted_data = sorted(data)
    mid = n // 2
    if n % 2 == 1:
        return sorted_data[mid]
    else:
        return (sorted_data[mid - 1] + sorted_data[mid]) / 2.0

if __name__ == '__main__':
    list1 = [1.5, 3.2, 2.8, 4.6, 5.9, 7.1, 8.3, 9.4, 10.0, 11.1]
    print(f"Median of {list1}: {calculate_median(list1)}")