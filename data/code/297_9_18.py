def validate_miles(miles):
    if miles < 0:
        raise ValueError("Miles cannot be negative")
    return miles

def convert_miles_to_kilometers(miles):
    validated_miles = validate_miles(miles)
    kilometers = validated_miles * 1.60934
    return kilometers

if __name__ == '__main__':
    sample_miles = 5
    result_km = convert_miles_to_kilometers(sample_miles)
    print(result_km)