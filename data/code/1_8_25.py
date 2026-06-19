def calculate_weighted_average(measurements, category_weights):
    if not measurements or not category_weights:
        return 0.0
    total_weight = sum(category_weights)
    weighted_sum = sum(m * w for m, w in zip(measurements, category_weights))
    return weighted_sum / total_weight

if __name__ == '__main__':
    sample_measurements = [10, 20, 30]
    sample_category_weights = [1, 2, 3]
    result = calculate_weighted_average(sample_measurements, sample_category_weights)
    print(result)