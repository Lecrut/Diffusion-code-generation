def convert_measurements(measurements, unit):
    meters_per_km = 1000.0
    feet_per_meter = 3.28084
    
    results = []
    
    for value in measurements:
        if unit == 'km':
            meters = value * meters_per_km
            feet = meters * feet_per_meter
        elif unit == 'm':
            meters = value
            feet = value * feet_per_meter
        elif unit == 'ft':
            feet = value
            meters = value / feet_per_meter
        else:
            continue
            
        results.append((value, unit, meters, feet))
        
    return results

def print_conversions(results):
    for original_value, original_unit, meters, feet in results:
        print(f"{original_value} {original_unit} = {meters:.2f} meters = {feet:.2f} feet")

if __name__ == '__main__':
    sample_measurements = [1.0, 5.5, 10.0]
    sample_unit = 'km'
    
    results = convert_measurements(sample_measurements, sample_unit)
    print_conversions(results)