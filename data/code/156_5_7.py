def calculate_average(numbers):
    if not all(isinstance(num, (int, float)) for num in numbers):
        raise ValueError("All elements must be numbers")
    return sum(numbers) / len(numbers)

if __name__ == '__main__':
    sample_numbers = [10, 20, 30, 40, 50]
    try:
        avg = calculate_average(sample_numbers)
        print(f"The average is: {avg}")
    except ValueError as e:
        print(e)