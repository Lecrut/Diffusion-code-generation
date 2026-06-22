WEIGHT_MIN_THRESHOLD = 0.0

def _is_valid_positive_weight(weight_string):
    try:
        parsed_value = float(weight_string)
        if parsed_value > WEIGHT_MIN_THRESHOLD:
            return parsed_value
        return None
    except (ValueError, TypeError):
        return None

def extract_valid_weights(measurements):
    return [
        value for measurement in measurements
        if (value := _is_valid_positive_weight(measurement)) is not None
    ]

if __name__ == '__main__':
    sample_data = ['10.5', '5.0', '-3.2', 'invalid', '0', '7.8', '', 'abc', '12', '  4.5  ', None, '  ']
    result = extract_valid_weights(sample_data)
    print(result)