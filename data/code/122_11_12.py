def validate_numbers(numbers):
    if not isinstance(numbers, tuple):
        raise TypeError("Input must be a tuple")
    for num in numbers:
        if not isinstance(num, int):
            raise ValueError("All elements in the tuple must be integers")

def calculate_average(numbers):
    validate_numbers(numbers)
    if len(numbers) == 0:
        return 0
    return sum(numbers) / len(numbers)

if __name__ == '__main__':
    sample_values = (10, 20, 30, 40, 50)
    average = calculate_average(sample_values)
    print(average)