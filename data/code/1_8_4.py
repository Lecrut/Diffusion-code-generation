def weighted_average(measurements: list, weights: list) -> float:
    total_weighted = sum(m * w for m, w in zip(measurements, weights))
    total_weight = sum(weights)
    if total_weight == 0:
        return 0.0
    return total_weighted / total_weight

if __name__ == '__main__':
    measurements = [10.0, 20.0, 30.0]
    weights = [1.0, 2.0, 5.0]
    result = weighted_average(measurements, weights)
    print(result)