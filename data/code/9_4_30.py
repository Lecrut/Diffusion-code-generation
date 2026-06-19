import argparse

def convert_volume(volume, from_unit, to_unit):
    conversion_factors = {
        'm3': {'m3': 1, 'liters': 1000, 'cubic_feet': 35.3147},
        'liters': {'m3': 0.001, 'liters': 1, 'cubic_feet': 0.035315},
        'cubic_feet': {'m3': 0.028317, 'liters': 28.3168, 'cubic_feet': 1}
    }
    
    if from_unit not in conversion_factors or to_unit not in conversion_factors[from_unit]:
        raise ValueError("Invalid unit conversion")
    
    return volume * conversion_factors[from_unit][to_unit]

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Volume Unit Converter')
    parser.add_argument('volume', type=float, help='The volume value to convert')
    parser.add_argument('from_unit', type=str, choices=['m3', 'liters', 'cubic_feet'], help='The starting unit of the volume')
    parser.add_argument('to_unit', type=str, choices=['m3', 'liters', 'cubic_feet'], help='The target unit to convert to')
    
    args = parser.parse_args()
    
    converted_volume = convert_volume(args.volume, args.from_unit, args.to_unit)
    print(converted_volume)