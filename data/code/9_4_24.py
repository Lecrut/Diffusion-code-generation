import argparse

def convert_volume(volume, from_unit, to_unit):
    conversion_factors = {'m3': {'m3': 1, 'cm3': 1000000, 'liters': 1000}, 'cm3': {'m3': 1e-06, 'cm3': 1, 'liters': 1}, 'liters': {'m3': 0.001, 'cm3': 1, 'liters': 1}}
    if from_unit not in conversion_factors or to_unit not in conversion_factors[from_unit]:
        return 'Invalid unit conversion'
    factor = conversion_factors[from_unit][to_unit]
    converted_volume = volume * factor
    return converted_volume
if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Volume Unit Converter')
    parser.add_argument('--volume', type=float, required=True, help='The volume to convert')
    parser.add_argument('--from_unit', type=str, required=True, choices=['m3', 'cm3', 'liters'], help='The starting unit of the volume')
    parser.add_argument('--to_unit', type=str, required=True, choices=['m3', 'cm3', 'liters'], help='The target unit to convert to')
    args = parser.parse_args()
    result = convert_volume(args.volume, args.from_unit, args.to_unit)
    print(result)
    sample_volume = 5.0
    sample_from_unit = 'm3'
    sample_to_unit = 'liters'
    sample_result = convert_volume(sample_volume, sample_from_unit, sample_to_unit)
    print(f'Sample conversion: {sample_volume} {sample_from_unit} to {sample_to_unit} is {sample_result}')