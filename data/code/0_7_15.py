def convert_length(value, unit):
    if unit == 'm':
        return value * 3.28084
    elif unit == 'ft':
        return value / 3.28084
    else:
        raise ValueError("Unsupported unit type")

if __name__ == '__main__':
    result = convert_length(1, 'm')
    print(result)
    result_ft = convert_length(3.28084, 'ft')
    print(result_ft)