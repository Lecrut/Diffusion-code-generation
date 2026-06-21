def calculate_weighted_average(measurements):
    if not measurements:
        raise ValueError("Measurements list cannot be empty")
    
    category_weights = {
        'category1': 0.2,
        'category2': 0.3,
        'category3': 0.5
    }
    
    total_weighted_sum = 0
    total_weight = 0
    
    for measurement, (value, category) in enumerate(measurements):
        if category not in category_weights:
            raise ValueError(f"Unsupported category: {category}")
        
        weight_factor = category_weights[category]
        weighted_value = value * weight_factor
        
        total_weighted_sum += weighted_value
        total_weight += weight_factor
    
    if total_weight == 0:
        raise ValueError("Total weight cannot be zero")
    
    return total_weighted_sum / total_weight

if __name__ == '__main__':
    sample_measurements = [
        (10, 'category1'),
        (20, 'category2'),
        (30, 'category3')
    ]
    result = calculate_weighted_average(sample_measurements)
    print(result)