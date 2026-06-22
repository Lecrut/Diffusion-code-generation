def calculate_median(data):
    n = len(data)
    if n == 0:
        raise ValueError("Input list cannot be empty")
    sorted_data = sorted(data)
    mid_index = n // 2
    if n % 2 == 1:
        median = sorted_data[mid_index]
    else:
        median = (sorted_data[mid_index - 1] + sorted_data[mid_index]) / 2.0
    return median

if __name__ == '__main__':
    sample_values = {
        "list1": [1, 3, 5, 7, 9],
        "list2": [4, 1, 8, 3, 6, 2]
    }
    
    for key, value in sample_values.items():
        print(f"Median of {key}: {calculate_median(value)}")