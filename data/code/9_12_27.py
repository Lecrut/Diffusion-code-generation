import argparse

def convert_volume(volume, input_unit, output_unit):
    conversion_factors = {
        'm3': {'m3': 1, 'liters': 1000},
        'liters': {'m3': 0.001, 'liters': 1}
    }
    
    if input_unit not in conversion_factors or output_unit not in conversion_factors[input_unit]:
        raise ValueError("Invalid unit conversion")
    
    return volume * conversion_factors[input_unit][output_unit]

def main():
    parser = argparse.ArgumentParser(description='Volume Unit Converter')
    parser.add_argument('--volume', type=float, required=True, help='Input volume')
    parser.add_argument('--input_unit', type=str, choices=['m3', 'liters'], required=True, help='Input unit (m3 or liters)')
    parser.add_argument('--output_unit', type=str, choices=['m3', 'liters'], required=True, help='Output unit (m3 or liters)')
    
    args = parser.parse_args()
    
    try:
        converted_volume = convert_volume(args.volume, args.input_unit, args.output_unit)
        print(converted_volume)
    except ValueError as e:
        print(e)

if __name__ == '__main__':
    main()