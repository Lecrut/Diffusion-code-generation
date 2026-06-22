def validate_input(data):
    for item in data:
        if not isinstance(item, int):
            raise ValueError("Invalid input detected: all elements must be integers.")

def calculate_total(numbers):
    try:
        validate_input(numbers)
        return sum(numbers)
    except ValueError as e:
        print(e)
        return None

if __name__ == '__main__':
    sample_numbers = (10, 20, 30, 40, 50)
    result = calculate_total(sample_numbers)
    print(result)