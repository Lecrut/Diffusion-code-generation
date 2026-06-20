def convert_length(value, unit):
    if unit == 'm':
        return value * 3.28084
    elif unit == 'ft':
        return value / 3.28084
    else:
        raise ValueError("Unsupported unit. Use 'm' for meters or 'ft' for feet.")

if __name__ == '__main__':
    print(convert_length(1, 'm'))
    print(convert_length(1, 'ft'))