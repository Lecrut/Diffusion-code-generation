def calculate_range(numbers):
    if not numbers:
        raise ValueError("No numbers provided.")
    return max(numbers) - min(numbers)

if __name__ == '__main__':
    sample_numbers = [10, 5, 22, 8, 15]
    try:
        range_val = calculate_range(sample_numbers)
        print(range_val)
    except ValueError as e:
        print(e)