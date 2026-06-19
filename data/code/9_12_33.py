import argparse

def convert_volume(volume, input_unit, output_unit):
    conversion_factors = {'mL': {'mL': 1, 'L': 0.001, 'gal': 0.000264172}, 'L': {'mL': 1000, 'L': 1, 'gal': 0.264172}, 'gal': {'mL': 3785.41, 'L': 3.78541, 'gal': 1}}
    if input_unit not in conversion_factors:
        raise ValueError(f'Unsupported input unit: {input_unit}')
    if output_unit not in conversion_factors[input_unit]:
        raise ValueError(f'Unsupported output unit: {output_unit}')
    return volume * conversion_factors[input_unit][output_unit]

def main():
    parser = argparse.ArgumentParser(description='Volume Unit Converter')
    parser.add_argument('--volume', type=float, required=True, help='Input volume')
    parser.add_argument('--input_unit', type=str, required=True, choices=['mL', 'L', 'gal'], help='Input unit (mL, L, gal)')
    parser.add_argument('--output_unit', type=str, required=True, choices=['mL', 'L', 'gal'], help='Output unit (mL, L, gal)')
    args = parser.parse_args()
    try:
        converted_volume = convert_volume(args.volume, args.input_unit, args.output_unit)
        print(converted_volume)
    except ValueError as e:
        print(e)
if __name__ == '__main__':
    volume = 1000
    input_unit = 'mL'
    output_unit = 'L'
    converted_volume = convert_volume(volume, input_unit, output_unit)
    print(converted_volume)