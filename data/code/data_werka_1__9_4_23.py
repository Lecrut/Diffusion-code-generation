import argparse

def convert_volume(volume, from_unit, to_unit):
    conversion_factors = {'ml': {'l': 0.001, 'gal': 0.00264172}, 'l': {'ml': 1000, 'gal': 0.264172}, 'gal': {'ml': 3785.41, 'l': 3.78541}}
    if from_unit not in conversion_factors or to_unit not in conversion_factors[from_unit]:
        raise ValueError('Invalid unit conversion')
    return volume * conversion_factors[from_unit][to_unit]

def main():
    parser = argparse.ArgumentParser(description='Volume Unit Converter')
    parser.add_argument('volume', type=float, help='The volume value to convert')
    parser.add_argument('from_unit', type=str, choices=['ml', 'l', 'gal'], help='The starting unit of the volume')
    parser.add_argument('to_unit', type=str, choices=['ml', 'l', 'gal'], help='The target unit for conversion')
    args = parser.parse_args()
    converted_volume = convert_volume(args.volume, args.from_unit, args.to_unit)
    print(converted_volume)
if __name__ == '__main__':
    volume = 1000.0
    from_unit = 'ml'
    to_unit = 'l'
    converted_volume = convert_volume(volume, from_unit, to_unit)
    print(converted_volume)