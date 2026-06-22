import argparse

def convert_volume(volume, input_unit, output_unit):
    conversion_factors = {'m3': 1, 'cm3': 1000000.0, 'dm3': 1000, 'l': 1000, 'ml': 1000000.0, 'ft3': 35.3147, 'in3': 61023.7}
    if input_unit not in conversion_factors or output_unit not in conversion_factors:
        raise ValueError('Invalid unit specified')
    volume_in_m3 = volume / conversion_factors[input_unit]
    converted_volume = volume_in_m3 * conversion_factors[output_unit]
    return converted_volume

def main():
    parser = argparse.ArgumentParser(description='Volume Unit Converter')
    parser.add_argument('volume', type=float, help='The volume value to convert')
    parser.add_argument('input_unit', type=str, help='The unit of the input volume (e.g., m3, cm3, dm3, l, ml, ft3, in3)')
    parser.add_argument('output_unit', type=str, help='The desired output unit (e.g., m3, cm3, dm3, l, ml, ft3, in3)')
    args = parser.parse_args()
    try:
        result = convert_volume(args.volume, args.input_unit, args.output_unit)
        print(result)
    except ValueError as e:
        print(e)
if __name__ == '__main__':
    volume = 1000.0
    input_unit = 'cm3'
    output_unit = 'm3'
    result = convert_volume(volume, input_unit, output_unit)
    print(result)