def calculate_weighted_average(measurements, weights):
    total_weight = sum(weights)
    weighted_sum = sum(m * w for m, w in zip(measurements, weights))
    return weighted_sum / total_weight

if __name__ == '__main__':
    measurements = [10, 20, 30, 40]
    weights = [1, 2, 3, 4]
    result = calculate_weighted_average(measurements, weights)
    print(result)