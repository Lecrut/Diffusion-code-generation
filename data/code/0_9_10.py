import math

def convert_measurements(measurements, unit):
    meters_list = []
    feet_list = []
    for value in measurements:
        if unit == 'kilometers':
            meters = value * 1000
        elif unit == 'meters':
            meters = value
        elif unit == 'centimeters':
            meters = value / 100
        elif unit == 'millimeters':
            meters = value / 1000
        elif unit == 'miles':
            meters = value * 1609.344
        elif unit == 'yards':
            meters = value * 0.9144
        elif unit == 'feet':
            meters = value / 3.28084
        elif unit == 'inches':
            meters = value / 39.3701
        else:
            raise ValueError(f"Unsupported unit: {unit}")
        
        feet = meters / 0.3048
        meters_list.append(meters)
        feet_list.append(feet)
    
    return meters_list, feet_list

if __name__ == '__main__':
    samples = [1.5, 2.0, 3.75]
    unit = 'kilometers'
    meters, feet = convert_measurements(samples, unit)
    print(meters)
    print(feet)