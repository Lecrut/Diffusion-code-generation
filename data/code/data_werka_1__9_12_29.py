import argparse

def convert_volume(input_volume, input_unit, output_unit):
    conversion_factors = {'m3': {'m3': 1, 'cm3': 1000000.0, 'liters': 1000}, 'cm3': {'m3': 1e-06, 'cm3': 1, 'liters': 1}, 'liters': {'m3': 0.001, 'cm3': 1, 'liters': 1}}
    if input_unit not in conversion_factors or output_unit not in conversion_factors[input_unit]:
        raise ValueError('Invalid unit conversion requested.')
    return input_volume * conversion_factors[input_unit][output_unit]

def main():
    parser = argparse.ArgumentParser(description='Volume Unit Converter')
    parser.add_argument('--input_volume', type=float, required=True)
    parser.add_argument('--input_unit', type=str, choices=['m3', 'cm3', 'liters'], required=True)
    parser.add_argument('--output_unit', type=str, choices=['m3', 'cm3', 'liters'], required=True)
    args = parser.parse_args()
    try:
        result = convert_volume(args.input_volume, args.input_unit, args.output_unit)
        print(result)
    except ValueError as e:
        print(f'Error: {e}')
if __name__ == '__main__':
    input_volume = 5.0
    input_unit = 'm3'
    output_unit = 'liters'
    result = convert_volume(input_volume, input_unit, output_unit)
    print(result)