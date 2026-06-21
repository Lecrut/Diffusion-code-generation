def get_unique_values(numbers):
    if not isinstance(numbers, list) or not all(isinstance(num, (int, float)) for num in numbers):
        raise ValueError("Input must be a list of numbers.")
    
    unique_numbers = dict.fromkeys(numbers)
    return set(unique_numbers.keys())

if __name__ == '__main__':
    sample_values = [1, 2, 3, 4, 5, 2, 3, 6]
    unique_set = get_unique_values(sample_values)
    print(unique_set)