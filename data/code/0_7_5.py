def convert_length(value, unit):
    if unit == 'm':
        return value * 3.28084
    elif unit == 'ft':
        return value * 0.3048
    else:
        raise ValueError("Invalid unit. Use 'm' for meters or 'ft' for feet.")

if __name__ == '__main__':
    print(convert_length(10, 'm'))
    print(convert_length(32.8084, 'ft'))