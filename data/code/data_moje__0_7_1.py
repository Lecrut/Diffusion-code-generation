def convert_length(value, unit):
    if unit == 'm':
        return value * 3.28084
    elif unit == 'ft':
        return value / 3.28084
    else:
        raise ValueError("Invalid unit. Use 'm' for meters or 'ft' for feet.")

if __name__ == '__main__':
    meters_value = 100
    feet_value = 328.084
    print(convert_length(meters_value, 'm'))
    print(convert_length(feet_value, 'ft'))