def meters_to_feet(meters):
    conversion_factor = 3.28084
    feet = meters * conversion_factor
    return feet

if __name__ == '__main__':
    sample_meters = 10
    result_feet = meters_to_feet(sample_meters)
    print(result_feet)