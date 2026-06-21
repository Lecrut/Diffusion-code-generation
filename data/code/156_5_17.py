def calculate_average(numbers):
    if not all(isinstance(num, (int, float)) for num in numbers):
        raise ValueError("One or more inputs were not valid numbers.")
    return sum(numbers) / len(numbers)

if __name__ == '__main__':
    sample_numbers = [10, 20, 30, 40, 50]
    try:
        average = calculate_average(sample_numbers)
        print(f"The calculated average is: {average}")
    except ValueError as e:
        print(e)