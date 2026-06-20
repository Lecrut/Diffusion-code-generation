def contains_negative(numbers):
    if not isinstance(numbers, list) or not all(isinstance(x, (int, float)) for x in numbers):
        raise ValueError("Input must be a list of numbers")
    
    return any(n < 0 for n in numbers)

if __name__ == '__main__':
    sample_values = [-1, 2, 3, -4, 5]
    result = contains_negative(sample_values)
    print(result)