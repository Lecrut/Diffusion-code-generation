def calculate_median(data):
    if not data:
        raise ValueError("Data list cannot be empty")
    
    sorted_data = sorted(data)
    n = len(sorted_data)
    
    if n % 2 == 1:
        return sorted_data[n // 2]
    else:
        mid1 = sorted_data[n // 2 - 1]
        mid2 = sorted_data[n // 2]
        return (mid1 + mid2) / 2

if __name__ == '__main__':
    samples = [
        [1, 5, 2, 8],
        [10, 20, 30, 40, 50],
        [7, 1, 4, 9, 2]
    ]
    
    for sample in samples:
        try:
            median_value = calculate_median(sample)
            print(f"Median of {sample} is {median_value}")
        except ValueError as e:
            print(e)