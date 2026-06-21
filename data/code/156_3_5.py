def calculate_mean(values):
    if not isinstance(values, list) or len(values) == 0:
        raise ValueError("Input must be a non-empty list of floats")
    total = sum(values)
    count = len(values)
    average = total / count
    return average

if __name__ == '__main__':
    sample_values = [2.1, 3.9, 4.7, 5.5]
    result = calculate_mean(sample_values)
    print(result)