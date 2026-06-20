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

    return mean, M2 / (n - 1) if n > 1 else float('nan')

if __name__ == '__main__':
    sample_sequence = [1.0, 2.0, 3.0, 4.0, 5.0]
    average, variance = welford_running_average(sample_sequence)
    print(f"Average: {average}, Variance: {variance}")