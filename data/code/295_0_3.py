import sys
def meters_to_feet(meters):
    return meters * 3.28084
def feet_to_meters(feet):
    return feet / 3.28084
if __name__ == '__main__':
    meters_value = 10.0
    feet_value = 50.0
    converted_feet = meters_to_feet(meters_value)
    converted_meters = feet_to_meters(feet_value)
    print(f"Meters to Feet conversion:")
    print(f"{meters_value} meters is equal to {converted_feet:.4f} feet")
    print("\nFeet to Meters conversion:")
    print(f"{feet_value} feet is equal to {converted_meters:.4f} meters")