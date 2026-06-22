def validate_numbers(numbers):
    if not all(isinstance(num, int) for num in numbers):
        raise ValueError("All elements in the list must be integers.")
    if len(numbers) == 0:
        raise ValueError("The list cannot be empty.")

def cycle_and_square(numbers):
    validate_numbers(numbers)
    for number in numbers:
        print(number ** 2)

if __name__ == '__main__':
    sample_values = [1, 2, 3, 4, 5]
    cycle_and_square(sample_values)