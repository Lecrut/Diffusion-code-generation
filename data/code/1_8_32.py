def weighted_average(measurements, category_weights):
    total_weight = sum(category_weights)
    if total_weight == 0:
        return 0
    weighted_sum = sum(m * w for m, w in zip(measurements, category_weights))
    return weighted_sum / total_weight

if __name__ == '__main__':
    measurements = [10, 20, 30, 40]
    category_weights = [1, 2, 3, 4]
    result = weighted_average(measurements, category_weights)
    print(result)