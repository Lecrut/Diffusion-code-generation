FEET_TO_INCHES_FACTOR = 12

def validate_feet(value):
    if not isinstance(value, (int, float)):
        raise TypeError("Input must be a number")
    if value < 0:
        raise ValueError("Input cannot be negative")

def feet_to_inches(feet):
    validate_feet(feet)
    return feet * FEET_TO_INCHES_FACTOR

if __name__ == '__main__':
    print(feet_to_inches(10))
    print(feet_to_inches(3.25))
    print(feet_to_inches(0))