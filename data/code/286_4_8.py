import re
def convert_to_feet(measurement):
    measurement = measurement.lower().strip()
    if not measurement:
        return None
    pattern = r"(\d+\.?\d*)\s*([a-zA-Z]+)"
    match = re.search(pattern, measurement)
    if not match:
        return None
    value_str = match.group(1)
    unit = match.group(2)
    try:
        value = float(value_str)
    except ValueError:
        return None
    conversion_factors = {
        'km': 32808.4,
        'm': 3.28084,
        'cm': 0.0328084,
        'in': 12,
        'ft': 12,
        'mile': 5280,
        'mi': 5280,
    }
    if unit in conversion_factors:
        if unit == 'km':
            return value * 32808.4
        elif unit == 'mi':
            return value * 5280
        else:
            if unit in ('m', 'cm'):
                feet = value * 3.28084
                return feet
            elif unit in ('ft', 'in'):
                if unit == 'ft':
                    return value
                elif unit == 'in':
                    return value / 12
            else:
                return None
    else:
        return None
if __name__ == '__main__':
    test_cases = [
        '10 km',
        '5 miles',
        '1000 m',
        '10 ft',
        '120 in',
        '1.5 km',
        '50000 cm',
        'invalid input',
        '2000',
        '3.5 mi'
    ]
    for test in test_cases:
        result = convert_to_feet(test)
        print(f"Input: '{test}' -> Output (feet): {result}")