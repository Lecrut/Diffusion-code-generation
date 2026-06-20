def calculate_weighted_average(measurements, category_weights):
    if not measurements or not category_weights:
        return 0.0
    if len(measurements) != len(category_weights):
        raise ValueError("Measurements and category weights must have the same length")
    
    total_weighted_sum = 0.0
    total_weight = 0.0
    
    for i in range(len(measurements)):
        value = measurements[i]
        weight = category_weights[i]
        if weight < 0:
            raise ValueError("Weights must be non-negative")
        total_weighted_sum += value * weight
        total_weight += weight
    
    if total_weight == 0:
        return 0.0
    
    return total_weighted_sum / total_weight

if __name__ == '__main__':
    sample_measurements = [10.0, 20.0, 30.0]
    sample_weights = [1.0, 2.0, 3.0]
    result = calculate_weighted_average(sample_measurements, sample_weights)
    print(result)