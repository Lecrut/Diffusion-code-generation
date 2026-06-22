CONVERSION_FACTORS = {
    'miles_to_feet': 5280,
    'feet_to_miles': 1/5280
}

def convert_distance(value, conversion_type):
    if conversion_type not in CONVERSION_FACTORS:
        raise ValueError("Invalid conversion type")
    return value * CONVERSION_FACTORS[conversion_type]

if __name__ == '__main__':
    sample_miles = 2.0
    sample_feet = 10560

    converted_feet = convert_distance(sample_miles, 'miles_to_feet')
    converted_miles = convert_distance(sample_feet, 'feet_to_miles')

    print(f"{sample_miles} miles is {converted_feet} feet")
    print(f"{sample_feet} feet is {converted_miles} miles")