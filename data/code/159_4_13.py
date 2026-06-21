def validate_input(numbers):
    if not all(isinstance(num, int) for num in numbers):
        raise ValueError("All elements in the list must be integers")
    return True

def find_odd_numbers(numbers):
    if not validate_input(numbers):
        return []
    return [num for num in numbers if num & 1]

if __name__ == '__main__':
    sample_values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print(find_odd_numbers(sample_values))