def calculate_weighted_average(measurements):
    if not isinstance(measurements, list) or not all(isinstance(m, tuple) and len(m) == 2 for m in measurements):
        raise ValueError("Measurements must be a list of tuples with two elements each")
    
    total_weight = sum(weight for _, weight in measurements)
    if total_weight == 0:
        raise ValueError("Total weight cannot be zero")
    
    weighted_sum = sum(measurement * weight for measurement, weight in measurements)
    return weighted_sum / total_weight

if __name__ == '__main__':
    sample_measurements = [
        (5, 1),
        (15, 2),
        (25, 3)
    ]
    result = calculate_weighted_average(sample_measurements)
    print(result)