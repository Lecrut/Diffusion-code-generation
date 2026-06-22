def compute_arithmetic_mean(values):
    total = 0.0
    count = 0
    for value in values:
        total += value
        count += 1
    if count == 0:
        return 0.0
    return total / count

if __name__ == '__main__':
    sample_values = [3.5, 7.2, 9.1, 4.8, 6.3]
    result = compute_arithmetic_mean(sample_values)
    print(result)