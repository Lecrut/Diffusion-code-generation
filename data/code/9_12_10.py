import argparse
import sys

def convert_volume(value, from_unit, to_unit):
    factors = {'l': 1.0, 'ml': 0.001, 'gal': 3.78541, 'pt': 0.473176, 'qt': 0.946353, 'cup': 0.236588, 'floz': 0.0295735, 'm3': 1000.0, 'cm3': 0.001}
    if from_unit not in factors:
        raise ValueError(f'Unknown input unit: {from_unit}')
    if to_unit not in factors:
        raise ValueError(f'Unknown output unit: {to_unit}')
    base_value = value * factors[from_unit]
    result = base_value / factors[to_unit]
    return result

def main():
    parser = argparse.ArgumentParser(description='Convert volume units')
    parser.add_argument('volume', type=float)
    parser.add_argument('from_unit', type=str)
    parser.add_argument('to_unit', type=str)
    args = parser.parse_args()
    result = convert_volume(args.volume, args.from_unit, args.to_unit)
    print(result)
if __name__ == '__main__':

    class SampleArgs:
        volume = 1.0
        from_unit = 'gal'
        to_unit = 'l'
    args = SampleArgs()
    result = convert_volume(args.volume, args.from_unit, args.to_unit)
    print(result)