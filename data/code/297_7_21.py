def cubic_meters_to_gallons(cubic_meters):
    conversion_factor = 264.172
    gallons = cubic_meters * conversion_factor
    return gallons

if __name__ == '__main__':
    sample_cubic_meters = 3
    result = cubic_meters_to_gallons(sample_cubic_meters)
    print(f"{sample_cubic_meters} cubic meters is equal to {result:.2f} gallons")