import tempfile
import os

def convert_volume(volume_value, unit):
    unit = unit.lower().strip()
    if unit in ('ml', 'milliliter', 'milliliters'):
        liters = volume_value / 1000.0
    elif unit in ('liters', 'liter', 'l'):
        liters = volume_value
    elif unit in ('cubic_meters', 'cubic_meter', 'm3', 'm^3'):
        liters = volume_value * 1000.0
    elif unit in ('gallons', 'gallon', 'gal'):
        liters = volume_value * 3.78541
    elif unit in ('cups', 'cup'):
        liters = volume_value * 0.236588
    elif unit in ('tablespoons', 'tablespoon', 'tbsp'):
        liters = volume_value * 0.0147868
    elif unit in ('teaspoons', 'teaspoon', 'tsp'):
        liters = volume_value * 0.00492892
    else:
        raise ValueError(f'Unsupported unit: {unit}')
    cubic_meters = liters / 1000.0
    return (liters, cubic_meters)

def process_volume_file(filepath):
    results = []
    try:
        with open(filepath, 'r') as file:
            for line_num, line in enumerate(file, 1):
                line = line.strip()
                if not line:
                    continue
                try:
                    parts = line.split()
                    if len(parts) != 2:
                        print(f"Line {line_num}: Invalid format. Expected 'value unit', got: {line}")
                        continue
                    value_str, unit = parts
                    value = float(value_str)
                    liters, cubic_meters = convert_volume(value, unit)
                    results.append((value, unit, liters, cubic_meters))
                except ValueError as ve:
                    print(f'Line {line_num}: Error parsing line - {ve}')
    except FileNotFoundError:
        print(f'Error: File not found - {filepath}')
    except PermissionError:
        print(f'Error: Permission denied - {filepath}')
    except IOError as e:
        print(f'Error reading file - {e}')
    return results

def print_results(results):
    if not results:
        print('No results to print.')
        return
    print(f"{'Original Value':>15} {'Original Unit':>15} {'Liters':>15} {'Cubic Meters':>15}")
    print('-' * 65)
    for value, unit, liters, cubic_meters in results:
        print(f'{value:>15.2f} {unit:>15} {liters:>15.6f} {cubic_meters:>15.9f}')
if __name__ == '__main__':
    sample_data = ['100 ml', '1 liters', '0.5 cubic_meters', '2 gallons', '8 cups', 'invalid_line', '50 ml']
    with tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.txt') as tmpfile:
        for line in sample_data:
            tmpfile.write(line + '\n')
        tmpfilepath = tmpfile.name
    try:
        results = process_volume_file(tmpfilepath)
        print_results(results)
    finally:
        os.unlink(tmpfilepath)