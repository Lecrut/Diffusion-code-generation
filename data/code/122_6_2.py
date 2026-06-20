def running_average_welford(values):
    mean = 0.0
    m2 = 0.0
    count = 0
    for value in values:
        count += 1
        delta = value - mean
        mean += delta / count
        delta2 = value - mean
        m2 += delta * delta2
    if count < 2:
        return None
    else:
        variance = m2 / (count - 1)
        std_dev = variance ** 0.5
        return (mean, std_dev)
if __name__ == '__main__':
    sample_values = [1.0, 2.0, 3.0, 4.0, 5.0]
    result = running_average_welford(sample_values)
    print(result)