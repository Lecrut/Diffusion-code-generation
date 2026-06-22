def weighted_average(values, weights):
    if sum(weights) == 0:
        raise ValueError("Sum of weights must be non-zero")
    return sum(v * w for v, w in zip(values, weights)) / sum(weights)

if __name__ == '__main__':
    sample_values = [45, 23, 17, 89]
    sample_weights = [0.3, 0.2, 0.1, 0.4]
    average = weighted_average(sample_values, sample_weights)
    print(average)