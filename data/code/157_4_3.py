def find_smallest_value(numbers):
    if not all(isinstance(n, int) for n in numbers):
        raise ValueError("All elements in the list must be integers")
    
    min_value = None
    for number in numbers:
        if min_value is None or number < min_value:
            min_value = number
    
    return min_value

if __name__ == '__main__':
    sample_values = [10, -3, 4, -7, 2]
    print(find_smallest_value(sample_values))