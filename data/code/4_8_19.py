import math

def convert_distance(value, source_unit, target_unit):
    conversion_factors = {
        ('km', 'mi'): 0.621371,
        ('mi', 'km'): 1.60934
    }
    unit_pair = (source_unit, target_unit)
    if unit_pair in conversion_factors:
        return value * conversion_factors[unit_pair]
    elif unit_pair[1] == unit_pair[0]:
        return value
    else:
        raise ValueError("Unsupported unit conversion")

def run_conversion_cli():
    sample_cases = [
        (10.0, 'km', 'mi'),
        (5.0, 'mi', 'km'),
        (100.0, 'km', 'mi'),
        (0.0, 'mi', 'km')
    ]
    results = []
    for val, src, tgt in sample_cases:
        try:
            converted = convert_distance(val, src, tgt)
            results.append(f"{val} {src} is {converted} {tgt}")
        except ValueError as e:
            results.append(f"Error converting {val} {src} to {tgt}: {e}")
    return results

if __name__ == '__main__':
    output_lines = run_conversion_cli()
    for line in output_lines:
        print(line)