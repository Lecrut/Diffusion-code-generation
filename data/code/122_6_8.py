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

    variance = M2 / (n - 1) if n > 1 else float('nan')
    return mean, variance

if __name__ == '__main__':
    sample_numbers = [1.0, 2.0, 3.0, 4.0, 5.0]
    avg, var = welford_running_average(sample_numbers)
    print(f"Running Average: {avg}")
    print(f"Variance: {var}")