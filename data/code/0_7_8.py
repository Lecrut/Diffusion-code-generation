def convert_length(value, unit):
    if unit == 'ft':
        return value * 0.3048
    return value

if __name__ == '__main__':
    meters = convert_length(10, 'm')
    print(meters)
    feet_to_meters = convert_length(3.28084, 'ft')
    print(feet_to_meters)