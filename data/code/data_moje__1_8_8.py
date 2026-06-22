def calculate_weighted_average(measurements, category_weights):
    if not measurements or not category_weights:
        return 0.0
    total_weighted_value = 0.0
    total_weight = 0.0
    for measurement, weight in zip(measurements, category_weights):
        total_weighted_value += measurement * weight
        total_weight += weight
    if total_weight == 0:
        return 0.0
    return total_weighted_value / total_weight

if __name__ == '__main__':
    sample_measurements = [75.5, 80.0, 70.0, 85.0]
    sample_category_weights = [1.0, 2.0, 1.5, 2.5]
    result = calculate_weighted_average(sample_measurements, sample_category_weights)
    print(result)