conversion_factor = 264.172

def cubic_meters_to_gallons(cubic_meters):
    return cubic_meters * conversion_factor

if __name__ == '__main__':
    sample_value1 = 5
    sample_value2 = 10
    print(f"{sample_value1} cubic meters is equal to {cubic_meters_to_gallons(sample_value1)} gallons")
    print(f"{sample_value2} cubic meters is equal to {cubic_meters_to_gallons(sample_value2)} gallons")