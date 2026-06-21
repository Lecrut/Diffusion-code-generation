def compute_mean(numbers):
    if not all(isinstance(num, (int, float)) for num in numbers):
        raise ValueError("All elements must be numeric")
    if len(numbers) == 0:
        return 0.0
    total = sum(numbers)
    count = len(numbers)
    return total / count

if __name__ == '__main__':
    sample_values = [10, 20, 30, 40, 50]
    print(f"Mean of {sample_values}: {compute_mean(sample_values)}")