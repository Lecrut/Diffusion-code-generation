def calculate_mean(numbers):
    if not numbers:
        raise ValueError("List must not be empty")
    return sum(numbers) / len(numbers)

if __name__ == '__main__':
    sample_values = [10.5, 20.25, 30.75, 40.0]
    result = calculate_mean(sample_values)
    print(result)