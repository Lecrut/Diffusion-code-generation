import sys
def meters_to_feet(meters):
    return meters * 3.28084
def feet_to_meters(feet):
    return feet / 3.28084
if __name__ == '__main__':
    meters_value = 10.0
    feet_value = 32.8084
    feet_from_meters = meters_to_feet(meters_value)
    meters_from_feet = feet_to_meters(feet_value)
    print(f"Conversion from {meters_value} meters to feet: {feet_from_meters}")
    print(f"Conversion from {feet_value} feet to meters: {meters_from_feet}")