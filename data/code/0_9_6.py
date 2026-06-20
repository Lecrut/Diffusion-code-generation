def convert_measurements(measurements, unit):
    if unit == 'km':
        factor_m = 1000
        factor_f = 3280.84
    elif unit == 'm':
        factor_m = 1
        factor_f = 3.28084
    elif unit == 'cm':
        factor_m = 0.01
        factor_f = 0.0328084
    elif unit == 'ft':
        factor_m = 0.3048
        factor_f = 1
    elif unit == 'in':
        factor_m = 0.0254
        factor_f = 0.0833333
    else:
        raise ValueError("Unsupported unit")
    
    results = []
    for value in measurements:
        meters = value * factor_m
        feet = value * factor_f
        results.append((value, meters, feet))
    return results

if __name__ == '__main__':
    sample_data = [1.5, 25, 0.001, 100]
    current_unit = 'km'
    output = convert_measurements(sample_data, current_unit)
    for original, meters, feet in output:
        print(f"{original} {current_unit} is {meters:.4f} meters and {feet:.4f} feet")