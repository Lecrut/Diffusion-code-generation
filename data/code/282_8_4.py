def calculate_total(numbers):
    if not all(isinstance(num, (int, float)) for num in numbers):
        raise ValueError("Error: All items must be integers or floats.")
    return sum(numbers)

if __name__ == '__main__':
    sample_numbers = [10, -5, 3.2, -2, 4]
    try:
        result = calculate_total(sample_numbers)
        print(result)
    except ValueError as e:
        print(e)