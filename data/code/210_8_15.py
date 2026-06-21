def calculate_range(data):
    if not data:
        raise ValueError("Data list cannot be empty")
    
    sorted_data = sorted(data)
    return sorted_data[-1] - sorted_data[0]

if __name__ == '__main__':
    sample_data = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
    print("Range of the dataset:", calculate_range(sample_data))