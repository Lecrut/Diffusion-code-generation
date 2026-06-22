import argparse

CONVERSION_FACTORS = {
    "m": 1.0,
    "km": 1000.0,
    "cm": 0.01,
    "mm": 0.001,
    "mi": 1609.344,
    "ft": 0.3048,
    "in": 0.0254,
    "yd": 0.9144,
    "nm": 1e-9,
}

def convert_volume_to_length(value, from_unit, to_unit):
    if from_unit not in CONVERSION_FACTORS or to_unit not in CONVERSION_FACTORS:
        raise ValueError("Unsupported unit")
    meters = value * CONVERSION_FACTORS[from_unit]
    result = meters / CONVERSION_FACTORS[to_unit]
    return result

def main():
    parser = argparse.ArgumentParser(description="Convert volume units to length units")
    parser.add_argument("volume", type=float, help="The volume value")
    parser.add_argument("from_unit", type=str, help="The starting unit")
    parser.add_argument("to_unit", type=str, help="The target unit")
    args = parser.parse_args([])
    
    args = type('obj', (object,), {
        'volume': 1000,
        'from_unit': 'cm',
        'to_unit': 'mm'
    })()
    
    result = convert_volume_to_length(args.volume, args.from_unit, args.to_unit)
    print(result)

if __name__ == '__main__':
    main()