def calculate_weighted_average(values, weights):
    if sum(weights) == 0:
        raise ValueError("Sum of weights must be non-zero")
    
    weighted_sum = sum(v * w for v, w in zip(values, weights))
    total_weights = sum(weights)
    
    return weighted_sum / total_weights

if __name__ == '__main__':
    sample_values = [15, 25, 35]
    sample_weights = [2, 4, 6]
    
    average = calculate_weighted_average(sample_values, sample_weights)
    print(average)