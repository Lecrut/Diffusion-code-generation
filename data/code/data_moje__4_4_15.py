def convert_distance(value: float, target_unit: str) -> float:
    units = {
        'm': 1.0,
        'km': 1000.0,
        'cm': 0.01,
        'mm': 0.001,
        'mi': 1609.344,
        'ft': 0.3048,
        'in': 0.0254,
        'yd': 0.9144,
        'nm': 1e-9,
    }
    if target_unit not in units:
        raise ValueError(f"Unsupported target unit: {target_unit}")
    result = value * units[target_unit]
    return result

def main():
    distance = 5.0
    target = 'km'
    converted = convert_distance(distance, target)
    print(converted)

if __name__ == '__main__':
    main()