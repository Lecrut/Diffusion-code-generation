def calculate_median(data):
    if not data:
        raise ValueError("Input list cannot be empty")
    sorted_data = sorted(data)
    n = len(sorted_data)
    mid_index = n // 2
    if n % 2 == 1:
        return sorted_data[mid_index]
    else:
        return (sorted_data[mid_index - 1] + sorted_data[mid_index]) / 2.0

if __name__ == '__main__':
    list1 = [3.5, 1.2, 8.9, 4.1, 2.3]
    print(f"Median of {list1}: {calculate_median(list1)}")