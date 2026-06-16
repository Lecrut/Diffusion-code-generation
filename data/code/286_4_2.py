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
        if unit in ('km', 'mi'):
            return value * conversion_factors[unit]
        elif unit in ('m', 'cm'):
            return value * 3.28084
        else:
            if unit in ('ft', 'in'):
                return value
            else:
                return None
    else:
        return None
if __name__ == '__main__':
    test_cases = [
        ('10 km', 32808.4),
        ('5 miles', 26400.0),
        ('1000 m', 3280.84),
        ('10 ft', 10.0),
        ('1 mile', 5280.0),
        ('100 cm', 3.28084),
        ('10000 in', 10000 / 12.0),
        ('50000 ft', 50000.0),
        ('invalid input', None)
    ]
    for input_str, expected in test_cases:
        result = convert_to_feet(input_str)
        print(f"Input: '{input_str}', Result: {result}, Expected: {expected}, Match: {result == expected}")