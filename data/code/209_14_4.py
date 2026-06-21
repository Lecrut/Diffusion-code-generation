def calculate_mean(samples):
    if not samples:
        raise ValueError("Input list cannot be empty")
    return sum(samples) / len(samples)

if __name__ == '__main__':
    test_samples = [15, 25, 35, 45, 55]
    print(calculate_mean(test_samples))