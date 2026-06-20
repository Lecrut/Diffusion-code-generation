def convert_length(value, unit):
    if unit == 'm':
        return value * 3.28084
    elif unit == 'ft':
        return value / 3.28084
    else:
        raise ValueError("Unsupported unit. Use 'm' for meters or 'ft' for feet.")

if __name__ == '__main__':
    sample_meters = 10
    sample_feet = 10
    result_from_meters = convert_length(sample_meters, 'm')
    result_from_feet = convert_length(sample_feet, 'ft')
    print(result_from_meters)
    print(result_from_feet)