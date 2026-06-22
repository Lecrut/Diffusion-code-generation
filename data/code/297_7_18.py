def cubic_meters_to_gallons(cubic_meters):
    conversion_factor = 264.172
    gallons = cubic_meters * conversion_factor
    return gallons

if __name__ == '__main__':
    sample_value = 3
    result = cubic_meters_to_gallons(sample_value)
    print(result)