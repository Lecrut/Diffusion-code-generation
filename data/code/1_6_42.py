def calculate_weighted_average(measurements):
    if not measurements:
        raise ValueError("Measurements list cannot be empty")
    
    weighted_sum = sum(measurement * weight for measurement, weight in measurements)
    total_weight = sum(weight for _, weight in measurements)
    
    if total_weight == 0:
        raise ValueError("Total weight cannot be zero")
    
    return weighted_sum / total_weight

if __name__ == '__main__':
    sample_measurements = [
        (10, 2),
        (25, 3),
        (40, 5)
    ]
    result = calculate_weighted_average(sample_measurements)
    print(result)