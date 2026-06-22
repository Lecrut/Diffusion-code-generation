def calculate_range(numbers):
    return max(numbers) - min(numbers)

if __name__ == '__main__':
    sample_values = [
        [3, 5, 1, 2],
        [-4, -1, -7, -3],
        [0.5, 0.2, 0.8, 0.1]
    ]
    
    for values in sample_values:
        print(f"Range of {values}: {calculate_range(values)}")