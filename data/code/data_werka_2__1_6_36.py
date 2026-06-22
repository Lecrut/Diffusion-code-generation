def weighted_average(measurements, weights):
    if len(measurements) != len(weights):
        raise ValueError("The length of measurements and weights must be the same.")
    
    total_weight = sum(weights)
    if total_weight == 0:
        raise ValueError("Total weight cannot be zero.")
    
    weighted_sum = sum(m * w for m, w in zip(measurements, weights))
    return weighted_sum / total_weight

if __name__ == '__main__':
    measurements = [10, 20, 30]
    weights = [1, 2, 3]
    result = weighted_average(measurements, weights)
    print(result)