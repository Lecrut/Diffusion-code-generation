def validate_numbers(numbers):
    if not all(isinstance(num, (int, float)) for num in numbers):
        raise ValueError("All elements in the sequence must be numbers")

def sum_large_sequence(numbers):
    validate_numbers(numbers)
    return sum(numbers)

if __name__ == '__main__':
    sample_numbers = [1.1, 2.2, 3.3, 4.4, 5.5]
    print(sum_large_sequence(sample_numbers))