def find_smallest_number(numbers):
    if not all(isinstance(num, (int, float)) for num in numbers):
        raise ValueError("All elements in the list must be integers or floats.")
    
    return min(numbers)

if __name__ == '__main__':
    sample_numbers = [3, -1, 4.5, 2, -3, 0]
    print(find_smallest_number(sample_numbers))