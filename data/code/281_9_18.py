def sum_of_twelve_numbers(numbers):
    if len(numbers) != 12:
        raise ValueError("Input set must contain exactly twelve numbers.")
    return sum(numbers)

if __name__ == '__main__':
    sample_numbers = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12}
    result = sum_of_twelve_numbers(sample_numbers)
    print(result)