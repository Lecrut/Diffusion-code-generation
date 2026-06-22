def validate_input(numbers):
    if not isinstance(numbers, tuple) or len(numbers) != 8:
        raise ValueError("Input must be a tuple of exactly eight numbers")

def sum_of_eight(numbers):
    validate_input(numbers)
    return sum(numbers)

if __name__ == '__main__':
    sample_values = (10, 20, 30, 40, 50, 60, 70, 80)
    print(sum_of_eight(sample_values))