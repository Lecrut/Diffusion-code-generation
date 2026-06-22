def validate_input(numbers_str):
    if not all(num.strip().isdigit() for num in numbers_str.split(',')):
        raise ValueError("Invalid input: All elements must be integers.")

def find_extremes(numbers_str):
    numbers = [int(num) for num in numbers_str.split(',')]
    smallest = min(numbers)
    largest = max(numbers)
    return smallest, largest

if __name__ == '__main__':
    sample_values = "3,1,4,1,5,9,2,6,5,3,5"
    validate_input(sample_values)
    result = find_extremes(sample_values)
    print(result)