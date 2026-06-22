def calculate_weighted_average(measurements):
    if not measurements:
        raise ValueError("Measurements list cannot be empty")
    
    WEIGHT_THRESHOLD = 0.01
    
    weighted_sum = sum(measurement * weight for measurement, weight in measurements)
    total_weight = sum(weight for _, weight in measurements)
    
    if abs(total_weight) < WEIGHT_THRESHOLD:
        raise ValueError("Total weight is too close to zero")
    
    return weighted_sum / total_weight

if __name__ == '__main__':
    sample_measurements = [
        (10, 2),
        (20, 3),
        (30, 5)
    ]
    result = calculate_weighted_average(sample_measurements)
    print(result)