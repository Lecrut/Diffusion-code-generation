def validate_input(numbers):
    if not all(isinstance(num, int) for num in numbers):
        raise ValueError("All elements in the list must be integers.")
    if not numbers:
        raise ValueError("The list cannot be empty.")

def calculate_total_sum(numbers):
    validate_input(numbers)
    return sum(numbers)

if __name__ == '__main__':
    sample_numbers = [10, 25, 5, 42, 18]
    total_sum = calculate_total_sum(sample_numbers)
    print(total_sum)