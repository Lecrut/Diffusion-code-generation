import sys

def convert_measurement(value, unit):
    if unit == 'kilometers':
        meters = value * 1000
        feet = value * 3280.84
    elif unit == 'meters':
        meters = value
        feet = value * 3.28084
    elif unit == 'feet':
        meters = value / 3.28084
        feet = value
    else:
        raise ValueError(f"Unsupported unit: {unit}")
    return meters, feet

def process_measurements(measurements, unit):
    results = []
    for val in measurements:
        m, f = convert_measurement(val, unit)
        results.append((m, f))
    return results

if __name__ == '__main__':
    sample_measurements = [1.5, 2.0, 0.5]
    sample_unit = 'kilometers'
    
    results = process_measurements(sample_measurements, sample_unit)
    
    for original, (meters, feet) in zip(sample_measurements, results):
        print(f"{original} {sample_unit} = {meters} meters, {feet} feet")