def compute_mean(numbers: list[int]) -> float:
    if not numbers:
        raise ValueError("Cannot compute mean of an empty list")
    return sum(numbers) / len(numbers)

if __name__ == '__main__':
    sample_numbers = [1, 2, 3, 4, 5]
    result = compute_mean(sample_numbers)
    print(result)