import argparse

def convert_volume(volume, input_unit, output_unit):
    conversion_factors = {'m3': {'m3': 1, 'liters': 1000, 'cubic_feet': 35.3147}, 'liters': {'m3': 0.001, 'liters': 1, 'cubic_feet': 0.035315}, 'cubic_feet': {'m3': 0.028317, 'liters': 28.3168, 'cubic_feet': 1}}
    if input_unit not in conversion_factors or output_unit not in conversion_factors[input_unit]:
        raise ValueError('Invalid unit conversion')
    return volume * conversion_factors[input_unit][output_unit]

def main():
    parser = argparse.ArgumentParser(description='Volume Unit Converter')
    parser.add_argument('--volume', type=float, required=True, help='Input volume value')
    parser.add_argument('--input_unit', type=str, choices=['m3', 'liters', 'cubic_feet'], required=True, help='Input unit (m3, liters, cubic_feet)')
    parser.add_argument('--output_unit', type=str, choices=['m3', 'liters', 'cubic_feet'], required=True, help='Output unit (m3, liters, cubic_feet)')
    args = parser.parse_args()
    try:
        converted_volume = convert_volume(args.volume, args.input_unit, args.output_unit)
        print(converted_volume)
    except ValueError as e:
        print(e)
if __name__ == '__main__':
    sample_volume = 10.0
    sample_input_unit = 'm3'
    sample_output_unit = 'liters'
    converted_value = convert_volume(sample_volume, sample_input_unit, sample_output_unit)
    print(converted_value)