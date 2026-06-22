def calculate_mean(numbers):
    if len(numbers) == 0:
        raise ValueError("Cannot calculate mean of an empty list")
    return sum(numbers) / len(numbers)

if __name__ == '__main__':
    sample_data = [1.5, 2.5, 3.0, 4.0]
    result = calculate_mean(sample_data)
    print(result)