def convert_length(value, unit):
    if unit == 'm':
        return value * 3.28084
    if unit == 'ft':
        return value / 3.28084
    raise ValueError("Invalid unit. Use 'm' for meters or 'ft' for feet.")

if __name__ == '__main__':
    print(convert_length(10, 'm'))
    print(convert_length(32.8084, 'ft'))