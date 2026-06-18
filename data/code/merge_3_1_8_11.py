def calculate_weighted_average(measurements):
    """
    Calculate the weighted average of a list of weight measurements, 
    where each measurement has an associated category weight (coefficient).
    
    Args:
        measurements (list[dict]): A list of dictionaries containing 'value' and 'weight'.
        
    Returns:
        float: The calculated weighted average.
    """
    total_weighted_value = 0.0
    total_coefficient = 0.0
    
    for item in measurements:
        value = item.get('value', 0)
        weight = item.get('weight', 1)
        
        if isinstance(value, (int, float)) and isinstance(weight, (int, float)):
            total_weighted_value += value * weight
            total_coefficient += abs(weight)

    return round(total_weighted_value / max(total_coefficient, 0.0), 6)

if __name__ == '__main__':
    sample_data = [
        {'value': 50.0, 'weight': 2},
        {'value': 75.0, 'weight': 3},
        {'value': 100.0, 'weight': 4},
        {'value': -20.0, 'weight': 1}
    ]

    result = calculate_weighted_average(sample_data)
    print(f"Weighted Average: {result}")