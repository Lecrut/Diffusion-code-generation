def calculate_mean(numbers):
    if not numbers:
        raise ValueError("Cannot calculate mean of an empty list")
    return sum(numbers) / len(numbers)

if __name__ == '__main__':
    sample_data = [1.0, 2.0, 3.0, 4.0, 5.0]
    result = calculate_mean(sample_data)
    print(result)