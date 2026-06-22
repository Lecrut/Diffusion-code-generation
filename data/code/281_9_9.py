def sum_of_twelve_numbers(numbers):
    if len(numbers) != 12:
        raise ValueError("The set must contain exactly twelve numbers.")
    return sum(numbers)

if __name__ == '__main__':
    sample_data = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12}
    try:
        result = sum_of_twelve_numbers(sample_data)
        print(f"Sum of twelve numbers: {result}")
    except ValueError as e:
        print(e)