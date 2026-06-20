def calculate_weighted_average(measurements, category_weights):
    if not measurements or not category_weights:
        return 0.0
    total_weight = 0.0
    weighted_sum = 0.0
    for measurement, weight in zip(measurements, category_weights):
        weighted_sum += measurement * weight
        total_weight += weight
    if total_weight == 0:
        return 0.0
    return weighted_sum / total_weight

if __name__ == '__main__':
    sample_measurements = [10.5, 12.3, 8.7, 15.2, 9.8]
    sample_category_weights = [1.0, 2.0, 1.5, 3.0, 0.5]
    result = calculate_weighted_average(sample_measurements, sample_category_weights)
    print(result)