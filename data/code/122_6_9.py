def welford_running_average(values):
    n = 0
    mean = 0.0
    M2 = 0.0
    for value in values:
        n += 1
        delta = value - mean
        mean += delta / n
        delta2 = value - mean
        M2 += delta * delta2
    if n < 2:
        return None
    variance = M2 / (n - 1)
    std_deviation = variance ** 0.5
    return mean, std_deviation

if __name__ == '__main__':
    sample_values = [10, 20, 30, 40, 50]
    result = welford_running_average(sample_values)
    print(result)