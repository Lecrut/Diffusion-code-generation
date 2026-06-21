def calculate_mean(samples):
    if not samples:
        raise ValueError("Input list cannot be empty")
    total_sum = sum(samples)
    count = len(samples)
    average = total_sum / count
    return average

if __name__ == '__main__':
    test_samples = [15, 25, 35, 45, 55]
    result = calculate_mean(test_samples)
    print(result)