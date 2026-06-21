def weighted_average(measurements, category_weights):
    if len(measurements) != len(category_weights):
        raise ValueError("The number of measurements must match the number of category weights.")
    
    total_weight = sum(category_weights)
    if total_weight == 0:
        raise ValueError("Total weight cannot be zero.")
    
    weighted_sum = sum(m * w for m, w in zip(measurements, category_weights))
    return weighted_sum / total_weight

if __name__ == '__main__':
    measurements = [10, 20, 30]
    category_weights = [1, 2, 3]
    result = weighted_average(measurements, category_weights)
    print(result)