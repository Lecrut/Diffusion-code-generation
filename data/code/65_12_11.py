FEET_TO_INCHES = 12
def feet_to_inches(feet):
    if not isinstance(feet, (int, float)):
        raise TypeError("Expected numeric value")
    if feet < 0:
        raise ValueError("Foot value must be non-negative")
    return feet * FEET_TO_INCHES

if __name__ == '__main__':
    feet = 10
    result = feet_to_inches(feet)
    print(result)