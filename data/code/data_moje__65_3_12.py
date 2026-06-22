CONVERSION_FACTOR = 12

def feet_to_inches(feet):
    unit_map = {
        "ft": 1,
        "feet": 1
    }
    factor = unit_map.get("ft", 1)
    return feet * factor * CONVERSION_FACTOR

if __name__ == '__main__':
    test_cases = [3, 7.5, 0, 12, 100]
    for value in test_cases:
        result = feet_to_inches(value)
        print(result)