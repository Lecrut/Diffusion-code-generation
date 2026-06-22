FEET_TO_INCHES_FACTOR = 12
UNIT_MAP = {"feet": FEET_TO_INCHES_FACTOR, "inch": 1, "yard": 36, "mile": 63360}

def convert_feet_to_inches(feet_value):
    factor = UNIT_MAP.get("feet", 1)
    return feet_value * factor

if __name__ == "__main__":
    test_cases = [1, 5, 10.5, 0]
    for val in test_cases:
        output = convert_feet_to_inches(val)
        print(output)