def compute_mean(samples):
    if not samples:
        raise ValueError("Input list cannot be empty")
    total = sum(samples)
    count = len(samples)
    average = total / count
    return average

if __name__ == '__main__':
    test_samples = [15, 25, 35, 45, 55]
    result = compute_mean(test_samples)
    print(result)