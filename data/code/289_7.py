def convert_meters_to_feet_and_miles(meters):
    feet = meters * 3.28084
    miles = feet * 0.0006535
    return feet, miles
if __name__ == '__main__':
    sample_meters = 10
    feet_result, miles_result = convert_meters_to_feet_and_miles(sample_meters)
    print(f"Input meters: {sample_meters}")
    print(f"Result in feet: {feet_result}")
    print(f"Result in miles: {miles_result}")