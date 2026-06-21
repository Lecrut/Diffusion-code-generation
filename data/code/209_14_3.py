def calculate_average(samples):
    if not samples:
        raise ValueError("Input list cannot be empty")
    
    total = sum(samples)
    count = len(samples)
    average = total / count
    
    return average

if __name__ == '__main__':
    test_samples = [25, 35, 45, 55, 65]
    result = calculate_average(test_samples)
    print(result)