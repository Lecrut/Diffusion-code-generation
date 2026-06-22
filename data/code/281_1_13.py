def validate_input(numbers):
    if not all(isinstance(num, (int, float)) for num in numbers) or len(numbers) != 4:
        raise ValueError("Input must be a list of exactly four floating-point numbers")

def calculate_sum(numbers):
    validate_input(numbers)
    return round(sum(numbers), 2)

if __name__ == '__main__':
    sample_data = [1.2345, 6.7890, 2.3456, 3.4567]
    result = calculate_sum(sample_data)
    print(result)