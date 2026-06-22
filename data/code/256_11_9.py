def calculate_range(numbers):
    return max(numbers) - min(numbers)

if __name__ == '__main__':
    sample_values = [3, 5, 1, 2, 4]
    print(calculate_range(sample_values))
    
    negative_values = [-7, -3, -5, -2]
    print(calculate_range(negative_values))
    
    floating_point_values = [3.5, 2.1, 4.8, 1.9]
    print(calculate_range(floating_point_values))