import argparse

def convert_volume(volume, input_unit, output_unit):
    conversion_factors = {'m3': 1, 'liters': 1000, 'cubic_feet': 35.3147, 'gallons': 264.172}
    if input_unit not in conversion_factors or output_unit not in conversion_factors:
        raise ValueError('Invalid unit provided')
    volume_in_m3 = volume / conversion_factors[input_unit]
    converted_volume = volume_in_m3 * conversion_factors[output_unit]
    return converted_volume

def main():
    parser = argparse.ArgumentParser(description='Volume Unit Converter')
    parser.add_argument('volume', type=float, help='The volume value to convert')
    parser.add_argument('input_unit', type=str, help='The unit of the input volume (m3, liters, cubic_feet, gallons)')
    parser.add_argument('output_unit', type=str, help='The desired output unit (m3, liters, cubic_feet, gallons)')
    args = parser.parse_args()
    try:
        result = convert_volume(args.volume, args.input_unit, args.output_unit)
        print(result)
    except ValueError as e:
        print(e)
if __name__ == '__main__':
    volume = 10.0
    input_unit = 'm3'
    output_unit = 'liters'
    result = convert_volume(volume, input_unit, output_unit)
    print(result)