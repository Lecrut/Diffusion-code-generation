def calculate_mean(values):
    if not isinstance(values, list) or len(values) == 0:
        raise ValueError("Input must be a non-empty list of floats")
    total = sum(values)
    count = len(values)
    average = total / count
    return average

if __name__ == '__main__':
    sample_values = [1.2, 2.8, 3.6, 4.4]
    result = calculate_mean(sample_values)
    print(result)