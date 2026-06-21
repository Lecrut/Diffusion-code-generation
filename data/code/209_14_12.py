def validate_samples(samples):
    if not samples:
        raise ValueError("Input list cannot be empty")

def calculate_mean(samples):
    total = sum(samples)
    count = len(samples)
    return total / count

if __name__ == '__main__':
    test_samples = [10, 20, 30, 40, 50]
    validate_samples(test_samples)
    result = calculate_mean(test_samples)
    print(result)