def meters_to_feet(meters):
    conversion_factor = 3.28084
    return meters * conversion_factor

if __name__ == '__main__':
    sample_value = 10
    result = meters_to_feet(sample_value)
    print(result)