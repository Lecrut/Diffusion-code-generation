def arithmetic_mean(values):
    total = 0.0
    for value in values:
        total += value
    count = len(values)
    if count == 0:
        raise ValueError("Cannot compute mean of empty sequence")
    return total / count

if __name__ == '__main__':
    sample_values = [10.5, 20.3, 30.1, 40.9, 50.2]
    result = arithmetic_mean(sample_values)
    print(result)