def calculate_weighted_average(measurements):
    if not measurements:
        return 0.0
    total_weighted_value = 0.0
    total_weights = 0.0
    for measurement, category_weight in measurements:
        total_weighted_value += measurement * category_weight
        total_weights += category_weight
    if total_weights == 0:
        return 0.0
    return total_weighted_value / total_weights

if __name__ == '__main__':
    sample_data = [
        (10.5, 2),
        (12.0, 3),
        (11.5, 1)
    ]
    result = calculate_weighted_average(sample_data)
    print(result)