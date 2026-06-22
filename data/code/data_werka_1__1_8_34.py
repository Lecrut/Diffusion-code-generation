def calculate_weighted_average(measurements):
    total_weight = 0
    weighted_sum = 0
    
    for value, weight in measurements:
        weighted_sum += value * weight
        total_weight += weight
    
    if total_weight == 0:
        return 0
    else:
        return weighted_sum / total_weight

if __name__ == '__main__':
    sample_measurements = [
        (10, 2),
        (20, 3),
        (30, 5)
    ]
    
    result = calculate_weighted_average(sample_measurements)
    print(result)