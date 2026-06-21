def calculate_weighted_average(measurements):
    if not measurements:
        raise ValueError("Measurements list cannot be empty")
    
    total_weight = 0
    weighted_sum = 0
    
    for measurement, weight in measurements:
        if weight < 0:
            raise ValueError("Weights must be non-negative")
        
        total_weight += weight
        weighted_sum += measurement * weight
    
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