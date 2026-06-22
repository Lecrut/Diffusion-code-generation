SUM_WEIGHTS_THRESHOLD = 1e-9

def weighted_average(values, weights):
    total_weight = sum(weights)
    if abs(total_weight) < SUM_WEIGHTS_THRESHOLD:
        raise ValueError("Sum of weights must be non-zero")
    return sum(v * w for v, w in zip(values, weights)) / total_weight

if __name__ == '__main__':
    values = [10, 20, 30]
    weights = [1, 2, 3]
    result = weighted_average(values, weights)
    print(result)