import re
def convert_to_feet(measurement):
    units = {
        'm': 3.28084,
        'km': 3280.84,
        'mi': 5280,
        'ft': 1,
        'in': 1/12,
        'yd': 3,
    }
    match = re.search(r"(\d+\.?\d*)\s*([a-zA-Z]+)", measurement)
    if not match:
        return None
    value_str = match.group(1)
    unit = match.group(2).lower()
    try:
        value = float(value_str)
    except ValueError:
        return None
    if unit in units:
        conversion_factor = units[unit]
        result = value * conversion_factor
        return result
    else:
        return None
if __name__ == '__main__':
    test_cases = [
        '10 km',
        '5 miles',
        '2000 m',
        '10 ft',
        '1 yard',
        '3.5 mi',
        '100 in',
        '500000 m'
    ]
    for test in test_cases:
        result = convert_to_feet(test)
        print(f"{test}: {result}")