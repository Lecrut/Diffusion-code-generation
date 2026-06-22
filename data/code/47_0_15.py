def calculate_mean(numbers):
    if not numbers:
        raise ValueError("Cannot calculate mean of an empty list")
    return sum(numbers) / len(numbers)

if __name__ == '__main__':
    sample_numbers = [1.5, 2.5, 3.5, 4.5, 5.5]
    result = calculate_mean(sample_numbers)
    print(result)