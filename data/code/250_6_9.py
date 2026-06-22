def weighted_average(values, weights):
    if sum(weights) == 0:
        raise ValueError("Sum of weights must be non-zero")
    return sum(v * w for v, w in zip(values, weights)) / sum(weights)

if __name__ == '__main__':
    VALUES = [10, 20, 30]
    WEIGHTS = [1, 2, 3]
    result = weighted_average(VALUES, WEIGHTS)
    print(result)