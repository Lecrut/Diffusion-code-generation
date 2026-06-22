CONVERSION_FACTOR = 5280

def miles_to_feet(miles):
    return miles * CONVERSION_FACTOR

def feet_to_miles(feet):
    return feet / CONVERSION_FACTOR

if __name__ == '__main__':
    sample_miles = 2.0
    sample_feet = 15840
    converted_feet = miles_to_feet(sample_miles)
    converted_miles = feet_to_miles(sample_feet)
    print(f"{sample_miles} miles is {converted_feet} feet")
    print(f"{sample_feet} feet is {converted_miles} miles")