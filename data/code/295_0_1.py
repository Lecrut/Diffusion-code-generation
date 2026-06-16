import sys
def convert_meters_to_feet(meters):
    return meters * 3.28084
if __name__ == '__main__':
    meters_value = 10.0
    feet_value = convert_meters_to_feet(meters_value)
    print(f"Meters: {meters_value}")
    print(f"Feet: {feet_value}")