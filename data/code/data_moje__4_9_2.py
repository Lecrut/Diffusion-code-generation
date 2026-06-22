def convert_distance(value, unit, conversion_factor):
    if unit == 'miles':
        return value * conversion_factor
    elif unit == 'kilometers':
        return value / conversion_factor
    else:
        raise ValueError("Unit must be 'miles' or 'kilometers'")

if __name__ == '__main__':
    sample_miles = 5.0
    miles_to_kms_factor = 1.60934
    sample_kilometers = 10.0
    kms_to_miles_factor = 1.60934
    
    converted_kms = convert_distance(sample_miles, 'miles', miles_to_kms_factor)
    converted_miles = convert_distance(sample_kilometers, 'kilometers', kms_to_miles_factor)
    
    print(converted_kms)
    print(converted_miles)