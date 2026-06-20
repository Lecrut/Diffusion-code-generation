import argparse

UNITS = {"m": 1, "km": 1000, "cm": 0.01, "mm": 0.001, "mi": 1609.344, "ft": 0.3048, "in": 0.0254, "yd": 0.9144}
BASE_UNITS = ("m", "km", "cm", "mm", "mi", "ft", "in", "yd")

def convert_distance(distance, from_unit, to_unit):
    if from_unit not in UNITS:
        raise ValueError(f"Invalid source unit: {from_unit}")
    if to_unit not in UNITS:
        raise ValueError(f"Invalid target unit: {to_unit}")
    if distance < 0:
        raise ValueError("Distance cannot be negative")
    
    base_distance = distance * UNITS[from_unit]
    result = base_distance / UNITS[to_unit]
    return result

def parse_args(args=None):
    parser = argparse.ArgumentParser(description="Convert distance between units")
    parser.add_argument("distance", type=float, help="Distance value to convert")
    parser.add_argument("from_unit", type=str, help="Source unit")
    parser.add_argument("to_unit", type=str, help="Target unit")
    
    if args is not None:
        return parser.parse_args(args)
    return parser.parse_args()

def main():
    args = parse_args(["1.0", "km", "mi"])
    
    try:
        result = convert_distance(args.distance, args.from_unit, args.to_unit)
        print(result)
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == '__main__':
    main()