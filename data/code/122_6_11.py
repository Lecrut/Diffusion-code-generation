def welford_running_average(sequence):
    n = 0
    mean = 0.0
    M2 = 0.0

    for value in sequence:
        n += 1
        delta = value - mean
        mean += delta / n
        delta2 = value - mean
        M2 += delta * delta2

    if n < 2:
        return None

    variance = M2 / (n - 1)
    std_dev = variance ** 0.5

    return mean, std_dev

if __name__ == '__main__':
    sample_sequence = [1.0, 2.0, 3.0, 4.0, 5.0]
    result = welford_running_average(sample_sequence)
    print(result)