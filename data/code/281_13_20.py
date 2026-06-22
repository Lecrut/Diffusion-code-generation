def validate_input(numbers):
    if not all(isinstance(num, int) for num in numbers):
        raise ValueError("All elements must be integers.")
    return numbers

def sum_of_integers(*args):
    validated_numbers = validate_input(args)
    total = 0
    for num in validated_numbers:
        total += num
    return total

if __name__ == '__main__':
    sample_values = [-10, -5, 0, 5, 10, 15]
    result = sum_of_integers(*sample_values)
    print(f"Sum of {sample_values}: {result}")