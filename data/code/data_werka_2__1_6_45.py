def validate_measurements(measurements):
    if not measurements:
        raise ValueError("Measurements list cannot be empty")
    for measurement, weight in measurements:
        if not isinstance(measurement, (int, float)) or not isinstance(weight, (int, float)):
            raise ValueError("Each measurement and weight must be a number")

def calculate_weighted_average(measurements):
    validate_measurements(measurements)
    weighted_sum = sum(measurement * weight for measurement, weight in measurements)
    total_weight = sum(weight for _, weight in measurements)
    if total_weight == 0:
        raise ValueError("Total weight cannot be zero")
    return weighted_sum / total_weight

if __name__ == '__main__':
    sample_measurements = [
        (5, 1),
        (15, 2),
        (25, 3)
    ]
    result = calculate_weighted_average(sample_measurements)
    print(result)