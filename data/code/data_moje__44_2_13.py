def arithmetic_mean(values):
    if not values:
        raise ValueError("Cannot compute mean of empty sequence")
    total = 0.0
    for value in values:
        total += value
    return total / len(values)

if __name__ == '__main__':
    sample_values = [1.5, 2.3, 3.7, 4.2, 5.1]
    result = arithmetic_mean(sample_values)
    print(result)