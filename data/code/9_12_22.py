import argparse

def convert_volume(volume, input_unit, output_unit):
    conversion_factors = {'m3': {'m3': 1, 'L': 1000}, 'L': {'m3': 0.001, 'L': 1}}
    if input_unit not in conversion_factors or output_unit not in conversion_factors[input_unit]:
        raise ValueError('Invalid unit conversion requested.')
    return volume * conversion_factors[input_unit][output_unit]

def main():
    parser = argparse.ArgumentParser(description='Volume Unit Converter')
    parser.add_argument('--volume', type=float, required=True, help='Input volume value')
    parser.add_argument('--input_unit', type=str, choices=['m3', 'L'], required=True, help='Input unit (m3 or L)')
    parser.add_argument('--output_unit', type=str, choices=['m3', 'L'], required=True, help='Output unit (m3 or L)')
    args = parser.parse_args()
    try:
        result = convert_volume(args.volume, args.input_unit, args.output_unit)
        print(result)
    except ValueError as e:
        print(e)
if __name__ == '__main__':
    sample_volume = 5.0
    sample_input_unit = 'm3'
    sample_output_unit = 'L'
    result = convert_volume(sample_volume, sample_input_unit, sample_output_unit)
    print(result)