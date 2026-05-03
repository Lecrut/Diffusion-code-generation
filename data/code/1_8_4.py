def calculate_weighted_average(measurements, category_weights):
    if not measurements or not category_weights:
        return 0
    total_weighted_sum = 0
    total_category_weight = 0
    for measurement, weight in zip(measurements, category_weights):
        total_weighted_sum += measurement * weight
        total_category_weight += weight
    if total_category_weight == 0:
        return 0
    return total_weighted_sum / total_category_weight
if __name__ == '__main__':
    measurements = [10, 20, 30]
    category_weights = [1.5, 2.0, 0.5]
    result = calculate_weighted_average(measurements, category_weights)
    print(result)