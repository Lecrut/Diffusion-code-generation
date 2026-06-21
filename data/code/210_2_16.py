def calculate_range(data):
    if not data:
        return None
    minimum = min(data)
    maximum = max(data)
    return maximum - minimum

if __name__ == '__main__':
    sample_data1 = [3, 7, 2, 5, 9]
    result1 = calculate_range(sample_data1)
    print(f"Data: {sample_data1}, Range: {result1}")
    
    sample_data2 = [100, 200, 300, 400, 500]
    result2 = calculate_range(sample_data2)
    print(f"Data: {sample_data2}, Range: {result2}")