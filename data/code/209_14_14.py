def calculate_mean(samples):
    if not samples:
        raise ValueError("Input list is empty")
    return sum(samples) / len(samples)

if __name__ == '__main__':
    test_samples = [10, 20, 30, 40, 50]
    try:
        mean_value = calculate_mean(test_samples)
        print(f"The mean of the samples is: {mean_value}")
    except ValueError as e:
        print(e)