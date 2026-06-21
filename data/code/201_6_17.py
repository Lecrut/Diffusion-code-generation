def compute_mean(numbers):
    if not all(isinstance(num, (int, float)) for num in numbers):
        raise ValueError("All elements must be numeric")
    return sum(numbers) / len(numbers)

if __name__ == '__main__':
    sample_data = [15, 25, 35, 45, 55]
    result = compute_mean(sample_data)
    print(f"Average: {result}")