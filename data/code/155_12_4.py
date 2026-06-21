def calculate_sum(numbers):
    if not isinstance(numbers, list):
        raise TypeError("Input must be a list")
    
    total_sum = 0.0
    for num in numbers:
        if not isinstance(num, (int, float)):
            print(f"Skipping invalid input: {num}")
        else:
            total_sum += num
    
    return total_sum

if __name__ == '__main__':
    sample_values = [10, 20, 35, 42]
    result = calculate_sum(sample_values)
    print(f"The total sum is: {result}")