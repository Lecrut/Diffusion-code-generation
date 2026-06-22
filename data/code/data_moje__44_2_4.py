def compute_arithmetic_mean(values):
    if not values:
        return 0.0
    total = 0.0
    for value in values:
        total += value
    return total / len(values)

if __name__ == '__main__':
    sample_values = [1.5, 2.5, 3.0, 4.5, 5.0]
    result = compute_arithmetic_mean(sample_values)
    print(result)