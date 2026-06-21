def calculate_average(numbers):
    NUMERICAL_ZERO = 0
    
    if not numbers:
        return None
    
    total_sum = sum(numbers)
    count = len(numbers)
    
    if count == NUMERICAL_ZERO:
        return None
    
    mean = total_sum / count
    return mean

if __name__ == '__main__':
    sample_values = [10, 20, 30, 40, 50]
    print(calculate_average(sample_values))