def convert_length(value, unit):
    if unit == 'm':
        return value * 3.28084
    elif unit == 'ft':
        return value * 0.3048
    else:
        return 0

if __name__ == '__main__':
    result1 = convert_length(1, 'm')
    print(result1)
    result2 = convert_length(1, 'ft')
    print(result2)