def arithmetic_mean(values):
    if len(values) == 0:
        raise ValueError("The list of values cannot be empty.")
    total = 0.0
    count = 0
    for value in values:
        total += value
        count += 1
    return total / count

if __name__ == '__main__':
    sample_values = [1.5, 2.5, 3.0, 4.0, 5.5]
    result = arithmetic_mean(sample_values)
    print(result)