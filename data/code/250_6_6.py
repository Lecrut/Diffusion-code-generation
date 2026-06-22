def weighted_average(values, weights):
    if sum(weights) == 0:
        raise ValueError("Sum of weights must be non-zero")
    return sum(value * weight for value, weight in zip(values, weights)) / sum(weights)

if __name__ == '__main__':
    values = [10, 20, 30]
    weights = [1, 2, 3]
    print(weighted_average(values, weights))