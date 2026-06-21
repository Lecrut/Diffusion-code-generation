def calculate_mean(values):
    if not values:
        return 0
    total = sum(values)
    count = len(values)
    mean = total / count
    return mean

if __name__ == '__main__':
    sample_data1 = [3, 6, 9, 12, 15]
    result1 = calculate_mean(sample_data1)
    print(f"Average of {sample_data1}: {result1}")
    
    sample_data2 = (7, 14, 21, 28)
    result2 = calculate_mean(sample_data2)
    print(f"Average of {sample_data2}: {result2}")
    
    sample_data3 = []
    result3 = calculate_mean(sample_data3)
    print(f"Average of {sample_data3}: {result3}")
    
    sample_data4 = [10]
    result4 = calculate_mean(sample_data4)
    print(f"Average of {sample_data4}: {result4}")