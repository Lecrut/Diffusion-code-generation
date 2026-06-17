import re
def convert_to_feet(measurement_string):
    pattern = r"(\d+\.?\d*)\s*(km|mi|m|ft|in)"
    match = re.search(pattern, measurement_string, re.IGNORECASE)
    if not match:
        return None
    value = float(match.group(1))
    unit = match.group(2).lower()
    conversion_factors = {
        'km': 3280.84,
        'mi': 5280,
        'm': 3.28084,
        'ft': 1,
        'in': 1/12
    }
    if unit == 'km':
        return value * 3280.84
    elif unit == 'mi':
        return value * 5280
    elif unit == 'm':
        return value * 3.28084
    elif unit == 'ft':
        return value
    elif unit == 'in':
        return value * (1/12)
    else:
        return None
if __name__ == '__main__':
    test_cases = [
        ('10 km', 32808.4),
        ('1 mile', 5280.0),
        ('1000 m', 3280.84),
        ('5 ft', 5.0),
        ('10 in', 0.8333333333333334),
        ('10 km', 32808.4),
        ('1 mi', 5280.0)
    ]
    for input_str, expected in test_cases:
        result = convert_to_feet(input_str)
        print(f"Input: '{input_str}', Result: {result}, Expected: {expected}, Match: {result == expected}")