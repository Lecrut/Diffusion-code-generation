def calculate_weighted_average(measurements, category_weights):
    if not measurements or not category_weights:
        raise ValueError("Measurements and category weights lists cannot be empty")
    if len(measurements) != len(category_weights):
        raise ValueError("Measurements and category weights lists must have the same length")
    total_weighted_value = 0
    total_weight = 0
    for value, weight in zip(measurements, category_weights):
        total_weighted_value += value * weight
        total_weight += weight
    if total_weight == 0:
        raise ZeroDivisionError("Total category weight cannot be zero")
    return total_weighted_value / total_weight

if __name__ == '__main__':
    sample_measurements = [10.5, 20.0, 15.5, 30.0]
    sample_category_weights = [1, 2, 1, 4]
    result = calculate_weighted_average(sample_measurements, sample_category_weights)
    print(result)