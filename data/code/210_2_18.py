MAX_VALUE = float('inf')
MIN_VALUE = float('-inf')

def calculate_range(data):
    if not data:
        return None
    minimum = MAX_VALUE
    maximum = MIN_VALUE
    for value in data:
        if value < minimum:
            minimum = value
        if value > maximum:
            maximum = value
    return maximum - minimum

if __name__ == '__main__':
    sample_data1 = [10, 5, 20, 15]
    result1 = calculate_range(sample_data1)
    print(f"Data: {sample_data1}, Range: {result1}")
    
    sample_data2 = [3, 1, 4, 1, 5, 9, 2, 6]
    result2 = calculate_range(sample_data2)
    print(f"Data: {sample_data2}, Range: {result2}")
    
    sample_data3 = []
    result3 = calculate_range(sample_data3)
    print(f"Data: {sample_data3}, Range: {result3}")