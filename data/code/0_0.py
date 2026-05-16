import sys
def meters_to_feet(meters):
    feet = meters * 3.28084
    return feet
if __name__ == '__main__':
    sample_meters = 10
    feet_result = meters_to_feet(sample_meters)
    print(f"{sample_meters} meters is equal to {feet_result} feet")