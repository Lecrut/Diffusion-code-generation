def convert_length(value: float, unit: str) -> float:
    if unit == 'm':
        return value
    elif unit == 'ft':
        return value * 0.3048
    elif unit == 'cm':
        return value * 0.01
    elif unit == 'in':
        return value * 0.0254
    else:
        raise ValueError(f"Unsupported unit: {unit}")

if __name__ == '__main__':
    meters = convert_length(10, 'm')
    feet = convert_length(3.28084, 'ft')
    centimeters = convert_length(50, 'cm')
    inches = convert_length(12, 'in')
    
    print(meters)
    print(feet)
    print(centimeters)
    print(inches)