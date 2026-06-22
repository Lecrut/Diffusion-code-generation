import argparse

def convert_volume(volume, from_unit, to_unit):
    conversion_factors = {'m3': {'m3': 1, 'L': 1000, 'gal': 264.172}, 'L': {'m3': 0.001, 'L': 1, 'gal': 0.264172}, 'gal': {'m3': 0.00378541, 'L': 3.78541, 'gal': 1}}
    if from_unit not in conversion_factors or to_unit not in conversion_factors[from_unit]:
        raise ValueError('Invalid unit conversion')
    return volume * conversion_factors[from_unit][to_unit]
if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Volume Unit Converter')
    parser.add_argument('--volume', type=float, required=True, help='The volume to convert')
    parser.add_argument('--from_unit', type=str, choices=['m3', 'L', 'gal'], required=True, help='The starting unit of the volume')
    parser.add_argument('--to_unit', type=str, choices=['m3', 'L', 'gal'], required=True, help='The target unit to convert to')
    args = parser.parse_args()
    converted_volume = convert_volume(args.volume, args.from_unit, args.to_unit)
    print(converted_volume)
    sample_volume = 10.0
    sample_from_unit = 'm3'
    sample_to_unit = 'gal'
    sample_converted_volume = convert_volume(sample_volume, sample_from_unit, sample_to_unit)
    print(f'Sample conversion: {sample_volume} {sample_from_unit} to {sample_to_unit} is {sample_converted_volume}')