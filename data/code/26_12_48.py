def validate_number(value):
    if not isinstance(value, (int, float)):
        raise ValueError("Value must be an integer or float")

def exceeds_threshold(value, threshold):
    validate_number(value)
    validate_number(threshold)
    return value > threshold

if __name__ == '__main__':
    sample_values = [
        (15, 10),
        (2.7, 3.0),
        (-1, -5),
        ('x', 1),
        (9, 'y')
    ]
    for value, threshold in sample_values:
        try:
            result = exceeds_threshold(value, threshold)
            print(f'Value: {value}, Threshold: {threshold} -> Exceeds: {result}')
        except Exception as e:
            print(f'Error with Value: {value}, Threshold: {threshold} -> {e}')