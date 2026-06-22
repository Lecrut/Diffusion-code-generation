def calculate_range(numbers):
    return max(numbers) - min(numbers)

if __name__ == '__main__':
    sample_values = [3, 5, 1, 2, 4]
    print(calculate_range(sample_values))
    
    sample_values = [-7, -3, -5, -2, -8]
    print(calculate_range(sample_values))
    
    sample_values = [0.5, 1.2, 3.4, 2.1, 0.9]
    print(calculate_range(sample_values))