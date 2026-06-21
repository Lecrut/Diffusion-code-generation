def safe_mean(numbers):
    if not isinstance(numbers, list) or not all(isinstance(n, (int, float)) for n in numbers):
        raise ValueError("Input must be a list of numbers")
    return sum(numbers) / len(numbers)

if __name__ == '__main__':
    sample_values = [3.5, 2.1, 4.8, 5.0]
    print(safe_mean(sample_values))