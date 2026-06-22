def convert_length(value, unit):
    if unit == 'm':
        return value * 3.28084
    elif unit == 'ft':
        return value / 3.28084
    return value

if __name__ == '__main__':
    print(convert_length(10, 'm'))
    print(convert_length(32.8084, 'ft'))