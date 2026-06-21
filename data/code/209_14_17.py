MIN_SAMPLES = 1

def calculate_mean(samples):
    if not samples:
        raise ValueError('Input list cannot be empty')
    total_sum = sum(samples)
    sample_count = len(samples)
    average = total_sum / sample_count
    return float(average)
if __name__ == '__main__':
    test_samples = [10, 20, 30, 40, 50]
    result = calculate_mean(test_samples)
    print(result)