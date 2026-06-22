import argparse

def convert_volume(volume, input_unit, output_unit):
    conversion_factors = {'m3': {'m3': 1, 'cm3': 1000000.0, 'ft3': 35.3147}, 'cm3': {'m3': 1e-06, 'cm3': 1, 'ft3': 0.035315}, 'ft3': {'m3': 0.028317, 'cm3': 28316.8, 'ft3': 1}}
    if input_unit not in conversion_factors or output_unit not in conversion_factors[input_unit]:
        raise ValueError('Invalid unit conversion')
    return volume * conversion_factors[input_unit][output_unit]

def main():
    parser = argparse.ArgumentParser(description='Volume Unit Converter')
    parser.add_argument('volume', type=float, help='The volume to convert')
    parser.add_argument('input_unit', type=str, choices=['m3', 'cm3', 'ft3'], help='The input unit (m3, cm3, ft3)')
    parser.add_argument('output_unit', type=str, choices=['m3', 'cm3', 'ft3'], help='The output unit (m3, cm3, ft3)')
    args = parser.parse_args()
    try:
        converted_volume = convert_volume(args.volume, args.input_unit, args.output_unit)
        print(converted_volume)
    except ValueError as e:
        print(e)
if __name__ == '__main__':
    volume = 10.0
    input_unit = 'm3'
    output_unit = 'ft3'
    converted_volume = convert_volume(volume, input_unit, output_unit)
    print(converted_volume)