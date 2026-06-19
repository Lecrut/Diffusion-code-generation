def check_value_exceeds_threshold(value, threshold):
    try:
        if not isinstance(value, (int, float)):
            raise TypeError("Value must be an integer or float.")
        if not isinstance(threshold, (int, float)):
            raise TypeError("Threshold must be an integer or float.")
        return value > threshold
    except Exception as e:
        print(f"Error: {e}")
        return False

if __name__ == '__main__':
    sample_values = [10, 20.5, -3, 'a', None]
    threshold = 15
    
    for val in sample_values:
        result = check_value_exceeds_threshold(val, threshold)
        print(f"Value: {val}, Threshold: {threshold}, Exceeds: {result}")