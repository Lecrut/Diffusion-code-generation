def validate_input(numbers):
    if not isinstance(numbers, list):
        raise ValueError("Input must be a list")
    if not all(isinstance(num, int) for num in numbers):
        raise ValueError("List elements must be integers")

def calculate_average(numbers):
    validate_input(numbers)
    if not numbers:
        return 0
    return sum(numbers) / len(numbers)

if __name__ == '__main__':
    sample_numbers = [10, 20, 30, 40, 50]
    print(calculate_average(sample_numbers))