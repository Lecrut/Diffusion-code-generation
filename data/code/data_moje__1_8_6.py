def weighted_average(measurements, category_weights):
    if not measurements or not category_weights:
        return 0.0
    total_weighted_sum = 0.0
    total_weight = 0.0
    for i, measurement in enumerate(measurements):
        weight = category_weights.get(i, 1.0)
        total_weighted_sum += measurement * weight
        total_weight += weight
    if total_weight == 0:
        return 0.0
    return total_weighted_sum / total_weight
if __name__ == '__main__':
    measurements = [70.5, 80.3, 90.1, 65.4, 88.9]
    category_weights = {0: 1.0, 1: 1.5, 2: 2.0, 3: 0.5, 4: 1.0}
    result = weighted_average(measurements, category_weights)
    print(result)