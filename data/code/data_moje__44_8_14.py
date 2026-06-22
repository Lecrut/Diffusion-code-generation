def compute_mean(numbers: list[int]) -> float:
    if not numbers:
        raise ValueError("Cannot compute mean of an empty list")
    return sum(numbers) / len(numbers)

if __name__ == '__main__':
    sample_values = [10, 20, 30, 40, 50]
    result = compute_mean(sample_values)
    print(result)