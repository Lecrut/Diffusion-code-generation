def calculate_range(numbers):
    return max(numbers) - min(numbers)

if __name__ == '__main__':
    sample_values = [3, 5, 1, 2, 4]
    print(calculate_range(sample_values))
    
    sample_values = [-7, -3, -9, -5, -1]
    print(calculate_range(sample_values))
    
    sample_values = [0.1, 0.5, 0.3, 0.8, 0.2]
    print(calculate_range(sample_values))