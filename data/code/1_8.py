def calculate_weighted_average(measurements, category_weights):
    total_weighted_sum = 0
    total_category_weight = 0
    if len(measurements) != len(category_weights):
        raise ValueError("Measurements and category weights must have the same length")
    for measurement, weight in zip(measurements, category_weights):
        total_weighted_sum += measurement * weight
        total_category_weight += weight
    if total_category_weight == 0:
        return 0
    else:
        return total_weighted_sum / total_category_weight
if __name__ == '__main__':
    sample_measurements = [10, 20, 30]
    sample_category_weights = [1.5, 2.0, 0.5]
    result = calculate_weighted_average(sample_measurements, sample_category_weights)
    print(result)