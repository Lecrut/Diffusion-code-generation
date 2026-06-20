import math

def convert_measurements(measurements, unit):
    results = []
    for measurement in measurements:
        value = float(measurement)
        meters = 0
        if unit == 'kilometers':
            meters = value * 1000
        elif unit == 'meters':
            meters = value
        elif unit == 'centimeters':
            meters = value / 100
        elif unit == 'millimeters':
            meters = value / 1000
        elif unit == 'inches':
            meters = value * 0.0254
        elif unit == 'feet':
            meters = value * 0.3048
        elif unit == 'yards':
            meters = value * 0.9144
        elif unit == 'miles':
            meters = value * 1609.344
        else:
            meters = 0
        feet = meters / 0.3048
        results.append({'original': value, 'unit': unit, 'meters': meters, 'feet': feet})
    return results

if __name__ == '__main__':
    sample_measurements = ['5', '100', '0.5', '10']
    sample_unit = 'kilometers'
    conversions = convert_measurements(sample_measurements, sample_unit)
    for conv in conversions:
        print(f"{conv['original']} {conv['unit']} = {conv['meters']} meters = {conv['feet']} feet")