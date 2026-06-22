def weighted_average(values, weights):
    if sum(weights) == 0:
        return None
    return sum(v * w for v, w in zip(values, weights)) / sum(weights)

if __name__ == '__main__':
    values = [10, 20, 30]
    weights = [1, 2, 3]
    result = weighted_average(values, weights)
    print(result)