def is_greater_than_threshold(value, threshold):
    return value > threshold

if __name__ == '__main__':
    sample_values = {
        'pi': 3.14,
        'e': 2.71,
        'golden_ratio': 1.618
    }
    
    threshold_value = 2.0
    
    for name, value in sample_values.items():
        result = is_greater_than_threshold(value, threshold_value)
        print(f"{name}: {value} > {threshold_value} -> {result}")