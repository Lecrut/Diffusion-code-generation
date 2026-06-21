def validate_numbers(numbers):
    if not all(isinstance(num, int) for num in numbers):
        raise ValueError("All elements in the list must be integers.")
    if len(numbers) == 0:
        raise ValueError("The list cannot be empty.")

def process_numbers(numbers):
    validate_numbers(numbers)
    for number in numbers:
        if number > 50:
            break
        if number % 2 == 0:
            continue
        print(number)

if __name__ == '__main__':
    sample_numbers = [3, 5, 8, 10, 23, 45, 60, 70]
    process_numbers(sample_numbers)