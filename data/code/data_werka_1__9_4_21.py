import argparse

def convert_volume(volume, from_unit, to_unit):
    conversion_factors = {
        'm3': {'m3': 1, 'liters': 1000},
        'liters': {'m3': 0.001, 'liters': 1}
    }
    
    if from_unit not in conversion_factors or to_unit not in conversion_factors[from_unit]:
        raise ValueError("Invalid unit conversion")
    
    return volume * conversion_factors[from_unit][to_unit]

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Volume Unit Converter')
    parser.add_argument('volume', type=float, help='The volume value to convert')
    parser.add_argument('from_unit', type=str, choices=['m3', 'liters'], help='The unit of the input volume')
    parser.add_argument('to_unit', type=str, choices=['m3', 'liters'], help='The target unit for conversion')
    
    args = parser.parse_args()
    
    converted_volume = convert_volume(args.volume, args.from_unit, args.to_unit)
    print(converted_volume)