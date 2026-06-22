def compute_arithmetic_mean(values):
    if not values:
        raise ValueError("Cannot compute mean of empty sequence")
    total = 0.0
    count = 0
    for value in values:
        total += value
        count += 1
    return total / count

if __name__ == '__main__':
    sample_values = [1.5, 2.7, 3.9, 4.2, 5.8]
    result = compute_arithmetic_mean(sample_values)
    print(result)