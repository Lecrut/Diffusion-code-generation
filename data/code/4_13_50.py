CONVERSION_FACTOR = 5280

def miles_to_feet(miles):
    if not isinstance(miles, (int, float)):
        raise ValueError("Input must be a number.")
    return miles * CONVERSION_FACTOR

def feet_to_miles(feet):
    if not isinstance(feet, (int, float)):
        raise ValueError("Input must be a number.")
    return feet / CONVERSION_FACTOR

if __name__ == '__main__':
    sample_miles = 2.5
    sample_feet = 14000
    try:
        converted_feet = miles_to_feet(sample_miles)
        converted_miles = feet_to_miles(sample_feet)
        print(f"{sample_miles} miles is {converted_feet} feet")
        print(f"{sample_feet} feet is {converted_miles} miles")
    except ValueError as e:
        print(e)