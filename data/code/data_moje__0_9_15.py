import sys

def convert_length_measurements(measurements, input_unit):
    conversion_factors = {
        'km': 1000.0,
        'm': 1.0,
        'cm': 0.01,
        'mm': 0.001,
        'mi': 1609.344,
        'ft': 0.3048,
        'in': 0.0254
    }
    
    base_unit_factor = conversion_factors.get(input_unit)
    if base_unit_factor is None:
        raise ValueError(f"Unsupported unit: {input_unit}")
    
    results = []
    for value in measurements:
        if not isinstance(value, (int, float)):
            raise TypeError("All measurements must be numeric")
        
        meters = value * base_unit_factor
        feet = meters / 0.3048
        results.append({
            'original': value,
            'unit': input_unit,
            'meters': meters,
            'feet': feet
        })
    
    return results

def print_conversions(results):
    for res in results:
        print(f"{res['original']} {res['unit']} is {res['meters']:.2f} meters and {res['feet']:.2f} feet")

if __name__ == '__main__':
    sample_measurements = [1.5, 10, 0.001, 5.5]
    sample_unit = 'km'
    
    converted_results = convert_length_measurements(sample_measurements, sample_unit)
    print_conversions(converted_results)