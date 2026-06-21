def find_maximum(numbers):
    if not isinstance(numbers, list) or not numbers:
        raise ValueError("Input must be a non-empty list of numbers")
    
    return max(numbers)

if __name__ == '__main__':
    sample_data = [10, 5, 22, 8, 30, 15]
    try:
        largest_number = find_maximum(sample_data)
        print(largest_number)
    except ValueError as e:
        print(e)