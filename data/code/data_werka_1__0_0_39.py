def convert_length(value: float, unit: str) -> float:
    if unit == 'm':
        return value
    elif unit == 'ft':
        return value * 0.3048
    elif unit == 'cm':
        return value * 0.01
    elif unit == 'km':
        return value * 1000
    elif unit == 'in':
        return value * 0.0254
    else:
        raise ValueError(f"Unsupported unit type: {unit}")

if __name__ == '__main__':
    meters_value = convert_length(10, 'm')
    feet_value = convert_length(10, 'ft')
    centimeters_value = convert_length(10, 'cm')
    print(meters_value)
    print(feet_value)
    print(centimeters_value)