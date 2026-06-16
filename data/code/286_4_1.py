import re
def convert_to_feet(measurement):
    pattern = r"(\d+\.?\d*)\s*([a-zA-Z]+)"
    match = re.search(pattern, measurement)
    if not match:
        return None
    value = float(match.group(1))
    unit = match.group(2).lower()
    conversion_factors = {
        'km': 3280.84,
        'm': 3.28084,
        'cm': 0.0328084,
        'in': 12,
        'ft': 12,
        'mile': 5280,
        'mi': 5280,
    }
    if unit in conversion_factors:
        return value * conversion_factors[unit]
    else:
        return None
if __name__ == '__main__':
    test_cases = [
        '10 km',
        '5 miles',
        '2000 m',
        '100 in',
        '1 ft',
        '50000 cm',
        '1.5 mi'
    ]
    for test in test_cases:
        result = convert_to_feet(test)
        print(f"{test}: {result}")