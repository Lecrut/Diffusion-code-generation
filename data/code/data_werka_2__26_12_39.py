def exceeds_threshold(value, threshold):
    if not isinstance(value, (int, float)):
        raise TypeError("Value must be an integer or float")
    if not isinstance(threshold, (int, float)):
        raise TypeError("Threshold must be an integer or float")
    return value > threshold

if __name__ == '__main__':
    sample_values = [
        (10, 5),
        (3.5, 4.0),
        ('a', 2),
        (7, 'b'),
        (8, 8)
    ]
    
    for value, threshold in sample_values:
        try:
            result = exceeds_threshold(value, threshold)
            print(f"Value: {value}, Threshold: {threshold} -> Exceeds: {result}")
        except Exception as e:
            print(f"Error with Value: {value}, Threshold: {threshold} -> {e}")