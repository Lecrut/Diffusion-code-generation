def validate_input(data):
    if not all(isinstance(num, (int, float)) for num in data):
        raise ValueError("All elements in the sequence must be numbers")

def sum_sequence(numbers):
    validate_input(numbers)
    return sum(numbers)

if __name__ == '__main__':
    sample_values = [1, 2, 3, 4, 5]
    result = sum_sequence(sample_values)
    print(result)