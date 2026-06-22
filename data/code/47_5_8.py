def calculate_mean(numbers):
    if not numbers:
        raise ValueError("List cannot be empty")
    return sum(numbers) / len(numbers)

if __name__ == '__main__':
    sample_values = [10, 20, 30, 40, 50]
    result = calculate_mean(sample_values)
    print(result)