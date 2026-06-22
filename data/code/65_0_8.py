FEET_TO_INCHES_FACTOR = 12

def feet_to_inches(feet):
    if not isinstance(feet, (int, float)):
        raise TypeError("Input must be a numeric value.")
    if feet < 0:
        raise ValueError("Feet value cannot be negative.")
    return feet * FEET_TO_INCHES_FACTOR

if __name__ == '__main__':
    print(feet_to_inches(10))
    print(feet_to_inches(3.5))
    print(feet_to_inches(0))