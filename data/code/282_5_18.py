def validate_numbers(numbers):
    if not all(isinstance(x, int) for x in numbers):
        raise ValueError("All elements must be integers.")

def sum_sequence_with_generator(numbers):
    return sum(x for x in numbers)

if __name__ == '__main__':
    sample_numbers = [1, 2, 3, 4, 5]
    validate_numbers(sample_numbers)
    result = sum_sequence_with_generator(sample_numbers)
    print(result)