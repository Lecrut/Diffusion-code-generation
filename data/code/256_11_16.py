def calculate_range(numbers):
    return max(numbers) - min(numbers)

if __name__ == '__main__':
    sample_values = [3, 5, 1, 2, 4]
    print(calculate_range(sample_values))
    
    negative_sample = [-7, -3, -5, -2]
    print(calculate_range(negative_sample))
    
    float_sample = [3.5, 2.1, 4.8, 1.9]
    print(calculate_range(float_sample))