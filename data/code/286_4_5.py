import re
def convert_to_feet(measurement_string):
    pattern = r"(\d+\.?\d*)\s*([a-zA-Z]+)"
    match = re.search(pattern, measurement_string)
    if not match:
        return None
    value = float(match.group(1))
    unit = match.group(2).lower()
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
        return value * conversion_factors[unit]
    else:
        return None
if __name__ == '__main__':
    test_cases = [
        ('10 km', None),
        ('5 miles', None),
        ('1000 m', None),
        ('12 ft', None),
        ('1 mile', None),
        ('100 in', None),
        ('50000 cm', None),
        ('1.5 km', None),
        ('7000 ft', None)
    ]
    results = {}
    for input_str, expected_result in test_cases:
        actual_result = convert_to_feet(input_str)
        results[input_str] = (actual_result, expected_result)
    print("--- Test Results ---")
    for input_str, (actual, expected) in results.items():
        print(f"Input: '{input_str}'")
        print(f"Actual: {actual}")
        print(f"Expected: {expected}")
        if actual == expected:
            print("Status: PASS\n")
        else:
            print("Status: FAIL\n")
    print("--- Specific Conversions ---")
    print(f"'10 km' -> {convert_to_feet('10 km')}")
    print(f"'5 miles' -> {convert_to_feet('5 miles')}")
    print(f"'1000 m' -> {convert_to_feet('1000 m')}")
    print(f"'12 ft' -> {convert_to_feet('12 ft')}")
    print(f"'1 mile' -> {convert_to_feet('1 mile')}")
    print(f"'100 in' -> {convert_to_feet('100 in')}")
    print(f"'50000 cm' -> {convert_to_feet('50000 cm')}")
    print(f"'1.5 km' -> {convert_to_feet('1.5 km')}")
    print(f"'7000 ft' -> {convert_to_feet('7000 ft')}")