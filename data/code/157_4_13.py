def find_smallest_value(numbers):
    if not isinstance(numbers, list) or not all(isinstance(n, (int, float)) for n in numbers):
        raise ValueError("Input must be a list of numeric values")
    
    return min(numbers)

if __name__ == '__main__':
    sample_values = [-5, 3, -1, 2, -4]
    print(find_smallest_value(sample_values))