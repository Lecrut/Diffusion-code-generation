def calculate_weighted_average(measurements):
    if not measurements:
        raise ValueError("Measurements list cannot be empty")
    
    def sum_weighted_values():
        total = 0
        for measurement, weight in measurements:
            total += measurement * weight
        return total

    def sum_weights():
        total = 0
        for _, weight in measurements:
            total += weight
        return total

    weighted_sum = sum_weighted_values()
    total_weight = sum_weights()

    if total_weight == 0:
        raise ValueError("Total weight cannot be zero")
    
    return weighted_sum / total_weight

if __name__ == '__main__':
    sample_measurements = [
        (15, 2),
        (25, 3),
        (35, 5)
    ]
    result = calculate_weighted_average(sample_measurements)
    print(result)