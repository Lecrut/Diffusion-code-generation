def convert_length(value, unit):
    if unit == 'ft':
        return value * 0.3048
    if unit == 'm':
        return value
    raise ValueError("Invalid unit")

if __name__ == '__main__':
    print(convert_length(10, 'ft'))
    print(convert_length(1, 'm'))