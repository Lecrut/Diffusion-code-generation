def validate_numbers(numbers):
    if not all(isinstance(num, int) for num in numbers):
        raise ValueError("All elements must be integers")
    if len(numbers) == 0:
        raise ValueError("The list cannot be empty")

def calculate_total_sum(numbers):
    validate_numbers(numbers)
    return sum(numbers)

if __name__ == '__main__':
    sample_numbers = [1, 2, 3, 4, 5]
    total_sum = calculate_total_sum(sample_numbers)
    print(total_sum)