def arithmetic_mean(values):
    total = 0.0
    count = 0
    for v in values:
        total += v
        count += 1
    if count == 0:
        return 0.0
    return total / count

if __name__ == '__main__':
    sample_values = [10.5, 20.3, 30.1, 40.9, 50.2]
    result = arithmetic_mean(sample_values)
    print(result)