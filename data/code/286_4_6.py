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
    if unit in conversion_factors:
        if unit == 'ft':
            return value
        else:
            return value * conversion_factors[unit]
    else:
        return None
if __name__ == '__main__':
    test_cases = [
        '10 km',
        '5 mi',
        '2000 m',
        '10 ft',
        '12 in',
        '1.5 km',
        '75000 ft'
    ]
    for test in test_cases:
        result = convert_to_feet(test)
        print(f"{test}: {result}")