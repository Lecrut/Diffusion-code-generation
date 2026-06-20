def calculate_average(numbers):
    if not isinstance(numbers, tuple) or not all(isinstance(num, int) for num in numbers):
        raise ValueError("Input must be a tuple of integers.")
    if not numbers:
        return 0
    return sum(numbers) / len(numbers)

if __name__ == '__main__':
    sample_values = (15, 25, 35, 45)
    try:
        average = calculate_average(sample_values)
        print(f"Average of {sample_values}: {average}")
    except ValueError as e:
        print(e)