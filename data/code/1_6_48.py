def calculate_weighted_average(measurements):
    if not measurements:
        raise ValueError("Measurements list cannot be empty")
    
    weighted_sum = 0
    total_weight = 0
    
    for measurement, weight in measurements:
        if weight < 0:
            raise ValueError("Weight cannot be negative")
        weighted_sum += measurement * weight
        total_weight += weight
    
    if total_weight == 0:
        raise ValueError("Total weight cannot be zero")
    
    return weighted_sum / total_weight

if __name__ == '__main__':
    sample_measurements = [
        (10, 2),
        (20, 3),
        (30, 5)
    ]
    result = calculate_weighted_average(sample_measurements)
    print(result)