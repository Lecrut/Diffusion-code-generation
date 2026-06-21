def calculate_range(data):
    if not data:
        raise ValueError("Input list is empty")
    if not all(isinstance(x, (int, float)) for x in data):
        raise ValueError("Input list contains non-numeric types")
    
    minimum = min(data)
    maximum = max(data)
    return maximum - minimum

if __name__ == '__main__':
    sample_data1 = [10, 5.5, 20, 3.14]
    print(f"Range of {sample_data1}: {calculate_range(sample_data1)}")
    
    sample_data2 = [-5, 100, 0.5, -10]
    print(f"Range of {sample_data2}: {calculate_range(sample_data2)}")
    
    sample_data3 = [7]
    print(f"Range of {sample_data3}: {calculate_range(sample_data3)}")
    
    sample_data4 = []
    try:
        print(f"Range of {sample_data4}: {calculate_range(sample_data4)}")
    except ValueError as e:
        print(e)