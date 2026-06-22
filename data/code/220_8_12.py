def calculate_average(numbers):
    if not hasattr(numbers, '__iter__') or isinstance(numbers, str):
        raise ValueError("Input must be an iterable of integers")
    
    total = sum(numbers)
    count = len(numbers)
    
    return float(total) / count

if __name__ == '__main__':
    sample_values = [10, 20, 30, 40, 50]
    print(calculate_average(sample_values))