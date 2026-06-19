def convert_length(value, unit):
    if unit == 'm':
        return value * 3.28084
    elif unit == 'ft':
        return value / 3.28084
    else:
        raise ValueError("Unsupported unit type")

if __name__ == '__main__':
    meters = convert_length(1, 'm')
    feet = convert_length(1, 'ft')
    print(meters)
    print(feet)