def welford_running_average(numbers):
    n = 0
    mean = 0.0
    M2 = 0.0

    for number in numbers:
        n += 1
        delta = number - mean
        mean += delta / n
        delta2 = number - mean
        M2 += delta * delta2

    if n < 2:
        return None

    variance = M2 / (n - 1)
    std_dev = variance ** 0.5
    return mean, std_dev

if __name__ == '__main__':
    sample_values = [4, 7, 13, 19]
    result = welford_running_average(sample_values)
    print(result)