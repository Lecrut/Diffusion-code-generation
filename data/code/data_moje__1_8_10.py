def calculate_weighted_average(measurements, category_weights):
    if not measurements or not category_weights:
        return 0.0
    if len(measurements) != len(category_weights):
        raise ValueError("Length of measurements and category_weights must match")
    total_weighted_sum = 0.0
    total_category_weight = 0.0
    for measurement, weight in zip(measurements, category_weights):
        total_weighted_sum += measurement * weight
        total_category_weight += weight
    if total_category_weight == 0:
        return 0.0
    return total_weighted_sum / total_category_weight

if __name__ == '__main__':
    sample_measurements = [70.5, 82.3, 65.1, 90.0]
    sample_category_weights = [0.2, 0.3, 0.1, 0.4]
    result = calculate_weighted_average(sample_measurements, sample_category_weights)
    print(result)