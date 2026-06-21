def calculate_average(numbers):
    if not numbers:
        raise ValueError("The list is empty")
    if not all(isinstance(num, (int, float)) for num in numbers):
        raise ValueError("All elements must be numeric")
    return sum(numbers) / len(numbers)

if __name__ == '__main__':
    sample_numbers = [10, 20, 30, 40, 50]
    try:
        avg = calculate_average(sample_numbers)
        print(avg)
    except ValueError as e:
        print(e)