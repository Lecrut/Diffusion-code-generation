CONVERSION_FACTOR = 5280

def validate_distance(value):
    if not isinstance(value, (int, float)):
        raise ValueError("Distance must be a number")
    if value < 0:
        raise ValueError("Distance cannot be negative")

def miles_to_feet(miles):
    validate_distance(miles)
    return miles * CONVERSION_FACTOR

def feet_to_miles(feet):
    validate_distance(feet)
    return feet / CONVERSION_FACTOR

if __name__ == '__main__':
    sample_miles = 2.5
    sample_feet = 13200
    try:
        converted_feet = miles_to_feet(sample_miles)
        converted_miles = feet_to_miles(sample_feet)
        print(f"{sample_miles} miles is {converted_feet} feet")
        print(f"{sample_feet} feet is {converted_miles} miles")
    except ValueError as e:
        print(e)