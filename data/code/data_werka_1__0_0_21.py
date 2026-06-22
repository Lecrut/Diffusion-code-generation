def convert_length(length: float, unit: str) -> float:
    conversions = {
        'm': 1.0,
        'ft': 0.3048,
        'cm': 0.01,
        'mm': 0.001,
        'km': 1000.0,
        'in': 0.0254,
        'yd': 0.9144,
    }

    if unit not in conversions:
        raise ValueError(f"Unsupported unit: {unit}")

    meters = length * conversions[unit]
    return meters

if __name__ == '__main__':
    result_meters = convert_length(10, 'm')
    print(result_meters)

    result_feet = convert_length(1, 'ft')
    print(result_feet)

    result_cm = convert_length(150, 'cm')
    print(result_cm)