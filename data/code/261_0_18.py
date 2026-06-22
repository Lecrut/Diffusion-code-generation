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
    sample_lists = [
        [5, 2, 8, 1, 9],
        [3, 7, 1, 4, 6, 2],
        [10, 20, 30, 40]
    ]
    
    for lst in sample_lists:
        median = calculate_median(lst)
        print(f"The median of {lst} is {median}")