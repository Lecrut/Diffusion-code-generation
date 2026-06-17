import math
def meters_to_feet(meters):
    return [m * 3.28084 for m in meters]
if __name__ == '__main__':
    measurements = [1.0, 5.5, 10.0, 100.0]
    feet_measurements = meters_to_feet(measurements)
    print(feet_measurements)