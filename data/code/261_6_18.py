def calculate_median(data):
    if not data:
        raise ValueError("Input list cannot be empty")
    sorted_data = sorted(data)
    n = len(sorted_data)
    mid_index = n // 2
    if n % 2 == 1:
        return sorted_data[mid_index]
    else:
        return (sorted_data[mid_index - 1] + sorted_data[mid_index]) / 2

if __name__ == '__main__':
    print(calculate_median([3, 1, 4, 1, 5, 9, 2]))