def weighted_average(values, weights):
    if sum(weights) == 0:
        raise ValueError("Sum of weights must be non-zero")
    return sum(v * w for v, w in zip(values, weights)) / sum(weights)

if __name__ == '__main__':
    values = [10, 20, 30]
    weights = [1, 2, 3]
    average = weighted_average(values, weights)
    print(average)