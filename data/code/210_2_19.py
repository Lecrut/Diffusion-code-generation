def calculate_range(data):
    if not data:
        return None
    minimum = min(data)
    maximum = max(data)
    return maximum - minimum

if __name__ == '__main__':
    sample_data1 = [3, 6, 2, 8, 4]
    range1 = calculate_range(sample_data1)
    print(f"Data: {sample_data1}, Range: {range1}")
    
    sample_data2 = [7, 7, 7, 7]
    range2 = calculate_range(sample_data2)
    print(f"Data: {sample_data2}, Range: {range2}")
    
    sample_data3 = []
    range3 = calculate_range(sample_data3)
    print(f"Data: {sample_data3}, Range: {range3}")