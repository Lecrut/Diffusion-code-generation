def convert_length(value, unit):
    if unit == 'm':
        return value * 3.28084
    elif unit == 'ft':
        return value / 3.28084
    else:
        raise ValueError("Invalid unit. Use 'm' for meters or 'ft' for feet.")

if __name__ == '__main__':
    result1 = convert_length(10, 'm')
    result2 = convert_length(32.8084, 'ft')
    print(result1)
    print(result2)