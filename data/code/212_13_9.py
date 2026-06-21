def find_min_max(numbers):
    if not isinstance(numbers, tuple) or not all(isinstance(x, int) for x in numbers):
        raise ValueError("Input must be a tuple of integers.")
    
    if len(numbers) == 0:
        return None
    
    minimum = min(numbers)
    maximum = max(numbers)
    
    return (minimum, maximum)

if __name__ == '__main__':
    sample_tuple = (10, 4, 25, 8, 30, 15)
    result = find_min_max(sample_tuple)
    print(result)