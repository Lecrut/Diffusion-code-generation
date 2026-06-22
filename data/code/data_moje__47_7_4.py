def compute_mean(numbers):
    if not numbers:
        raise ValueError("Cannot compute mean of an empty list")
    return sum(numbers) / len(numbers)

if __name__ == '__main__':
    sample_list = [10, 20, 30, 40, 50]
    result = compute_mean(sample_list)
    print(result)