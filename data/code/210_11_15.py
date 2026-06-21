def calculate_data_range(data):
    if not data:
        raise ValueError("Input list cannot be empty.")
    min_value = float('inf')
    max_value = float('-inf')
    for value in data:
        if value < min_value:
            min_value = value
        if value > max_value:
            max_value = value
    return max_value - min_value

if __name__ == '__main__':
    sample_data1 = [3, 7, 2, 9, 5]
    sample_data2 = [4.5, 1.2, 8.8, 0.1]
    empty_list = []

    try:
        range1 = calculate_data_range(sample_data1)
        print(f"Data: {sample_data1}, Range: {range1}")
        range2 = calculate_data_range(sample_data2)
        print(f"Data: {sample_data2}, Range: {range2}")
        calculate_data_range(empty_list)
    except ValueError as e:
        print(f"Error caught: {e}")