def calculate_weighted_average(measurements, category_weights):
    if not measurements or not category_weights:
        return 0.0
    if len(measurements) != len(category_weights):
        raise ValueError("Measurements and category weights must have the same length")
    total_weighted_value = 0.0
    total_weights = 0.0
    for i in range(len(measurements)):
        value = measurements[i]
        weight = category_weights[i]
        total_weighted_value += value * weight
        total_weights += weight
    if total_weights == 0:
        return 0.0
    return total_weighted_value / total_weights

if __name__ == '__main__':
    sample_measurements = [10.5, 20.0, 15.5, 30.0]
    sample_weights = [1, 2, 1, 4]
    result = calculate_weighted_average(sample_measurements, sample_weights)
    print(result)