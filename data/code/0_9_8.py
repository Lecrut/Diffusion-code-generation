import sys

def convert_lengths(measurements, unit):
    conversion_factors = {
        "kilometer": 1000.0,
        "meter": 1.0,
        "centimeter": 0.01,
        "millimeter": 0.001,
        "foot": 0.3048,
        "inch": 0.0254,
        "yard": 0.9144,
        "mile": 1609.34
    }
    
    unit_lower = unit.lower()
    if unit_lower not in conversion_factors:
        raise ValueError(f"Unsupported unit: {unit}")
    
    factor_to_meters = conversion_factors[unit_lower]
    factor_from_meters_to_feet = 3.28084
    
    results = []
    for value in measurements:
        if not isinstance(value, (int, float)):
            raise TypeError(f"Invalid measurement value: {value}")
        
        meters = value * factor_to_meters
        feet = meters * factor_from_meters_to_feet
        results.append((meters, feet))
    
    return results

def format_output(measurements, unit):
    try:
        converted = convert_lengths(measurements, unit)
    except (ValueError, TypeError) as e:
        return [f"Error: {e}"]
    
    output_lines = []
    for i, (meters, feet) in enumerate(converted):
        original_val = measurements[i]
        output_lines.append(f"{original_val} {unit} = {meters:.4f} meters, {feet:.4f} feet")
    
    return output_lines

if __name__ == '__main__':
    sample_data = [1.0, 5.5, 0.001, 100]
    sample_unit = "kilometer"
    results = format_output(sample_data, sample_unit)
    for line in results:
        print(line)