FEET_PER_MILE = 5280

def _validate_miles(value):
    if not isinstance(value, (int, float)):
        raise TypeError("Miles must be a number")
    if value < 0:
        raise ValueError("Miles cannot be negative")
    return value

def miles_to_feet(miles):
    validated_miles = _validate_miles(miles)
    return validated_miles * FEET_PER_MILE

if __name__ == '__main__':
    print(miles_to_feet(1))
    print(miles_to_feet(3.5))