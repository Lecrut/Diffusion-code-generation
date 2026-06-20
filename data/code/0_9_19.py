import math

def convert_units(values_in_kilometers):
    meter_multiplier = 1000
    feet_per_meter = 3.28084
    results = []
    for val in values_in_kilometers:
        meters = val * meter_multiplier
        feet = val * meter_multiplier * feet_per_meter
        results.append({'km': val, 'm': meters, 'ft': feet})
    return results

if __name__ == '__main__':
    sample_kilometers = [1.5, 10.0, 0.001]
    converted_data = convert_units(sample_kilometers)
    for item in converted_data:
        print(f"{item['km']} km = {item['m']} m = {item['ft']} ft")