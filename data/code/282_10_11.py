def validate_numbers(numbers):
    if not all(isinstance(num, (int, float)) for num in numbers):
        raise ValueError("All elements must be numbers")

def calculate_sequence_sum(numbers):
    validate_numbers(numbers)
    return sum([num for num in numbers])

if __name__ == '__main__':
    data = [1, 5, 10, 15, 20]
    result = calculate_sequence_sum(data)
    print(result)