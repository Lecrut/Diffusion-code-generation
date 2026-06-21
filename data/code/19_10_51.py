def is_positive(number):
    if not isinstance(number, int):
        raise ValueError("Input must be an integer")
    return number > 0

def validate_input(value):
    if not isinstance(value, int):
        raise ValueError(f"Invalid input: {value} is not an integer")

if __name__ == '__main__':
    sample_values = [15, -3, 0, 8, -6]
    results = {}
    for value in sample_values:
        try:
            validate_input(value)
            results[value] = is_positive(value)
        except ValueError as e:
            results[value] = str(e)
    print(results)