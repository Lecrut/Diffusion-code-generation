import math
WELFORD_EPSILON = 1e-07

def running_average_welford(values):
    n = 0
    mean = 0.0
    m2 = 0.0
    for value in values:
        n += 1
        delta = value - mean
        mean += delta / (n + WELFORD_EPSILON)
        delta2 = value - mean
        m2 += delta * delta2
    if n < 2:
        return None
    variance = m2 / (n - 1)
    std_deviation = math.sqrt(variance)
    return (mean, std_deviation)
if __name__ == '__main__':
    sample_values = [3.0, 7.5, 9.0, 4.5, 6.0]
    result = running_average_welford(sample_values)
    print(result)