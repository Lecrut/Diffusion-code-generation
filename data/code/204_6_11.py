def find_median(data):
    if len(data) != 3:
        raise ValueError("Input list must contain exactly three integers")
    
    sorted_data = sorted(data)
    return sorted_data[1]

if __name__ == '__main__':
    sample_values = [
        [3, 1, 4],
        [10, 5, 15],
        [7, 2, 4],
        [1, 2, 3]
    ]
    
    for values in sample_values:
        print(f"Median of {values}: {find_median(values)}")