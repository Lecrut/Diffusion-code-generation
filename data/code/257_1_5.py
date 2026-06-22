def validate_input(numbers):
    if not numbers:
        raise ValueError("The tuple must contain at least one number.")
    for num in numbers:
        if not isinstance(num, float):
            raise TypeError("All elements in the tuple must be floating-point numbers.")

def find_difference(numbers):
    validate_input(numbers)
    return max(numbers) - min(numbers)

if __name__ == '__main__':
    sample_values = (3.5, 1.2, 4.8, 2.9)
    print(find_difference(sample_values))