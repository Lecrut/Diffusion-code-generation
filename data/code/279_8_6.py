def cycle_and_square(numbers):
    if not all(isinstance(num, int) for num in numbers):
        raise ValueError("All elements in the list must be integers.")
    
    squared_values = [num ** 2 for num in numbers]
    return squared_values

if __name__ == '__main__':
    sample_values = [1, 2, 3, 4, 5]
    result = cycle_and_square(sample_values)
    print(result)