def calculate_average(numbers):
    if not isinstance(numbers, list) or not all(isinstance(x, (int, float)) for x in numbers):
        raise ValueError("Input must be a list of numerical values.")
    return sum(numbers) / len(numbers)

if __name__ == '__main__':
    sample_values = [10, 20, 30, 40, 50]
    try:
        result = calculate_average(sample_values)
        print(result)
    except ValueError as e:
        print(e)