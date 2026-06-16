import sys
def meters_to_feet(meters):
    return meters * 3.28084
def feet_to_meters(feet):
    return feet / 3.28084
if __name__ == '__main__':
    meters_value = 10.0
    feet_value = 32.8084
    print(f"Meters to Feet Conversion:")
    result_feet = meters_to_feet(meters_value)
    print(f"{meters_value} meters is equal to {result_feet} feet")
    print("\nFeet to Meters Conversion:")
    result_meters = feet_to_meters(feet_value)
    print(f"{feet_value} feet is equal to {result_meters} meters")