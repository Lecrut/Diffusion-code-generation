def calculate_range(numbers):
    return max(numbers) - min(numbers)

if __name__ == '__main__':
    sample_values = [3, 5, 1, 2, 4]
    print(calculate_range(sample_values))
    
    negative_values = [-7, -3, -9, -5, -2]
    print(calculate_range(negative_values))
    
    floating_point_values = [3.5, 2.1, 5.6, 0.8, 4.3]
    print(calculate_range(floating_point_values))