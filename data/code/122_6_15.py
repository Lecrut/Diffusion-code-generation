def welford_running_average(numbers):
    mean = 0.0
    m2 = 0.0
    count = 0

    for number in numbers:
        count += 1
        delta = number - mean
        mean += delta / count
        delta2 = number - mean
        m2 += delta * delta2

    variance = m2 / (count - 1) if count > 1 else float('nan')
    return mean, variance

if __name__ == '__main__':
    sample_values = [1.0, 2.0, 3.0, 4.0, 5.0]
    avg, var = welford_running_average(sample_values)
    print(f"Running average: {avg}")
    print(f"Variance: {var}")