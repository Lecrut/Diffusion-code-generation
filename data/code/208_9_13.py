def calculate_mean(numbers):
    if not numbers:
        raise ValueError("Cannot calculate the mean of an empty list")
    return sum(numbers) / len(numbers)

if __name__ == '__main__':
    sample_values = (1, 2, 3, 4)
    try:
        result = calculate_mean(sample_values)
        print(result)
    except ValueError as e:
        print(e)