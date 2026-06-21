def calculate_range(data):
    if not data:
        raise ValueError("Data list cannot be empty")
    min_val = max_val = data[0]
    for item in data[1:]:
        if item < min_val:
            min_val = item
        elif item > max_val:
            max_val = item
    return max_val - min_val

if __name__ == '__main__':
    sample_data = [3, 5, 1, 2, 4, 8, 7, 6]
    range_result = calculate_range(sample_data)
    print(f"The range of the data is: {range_result}")