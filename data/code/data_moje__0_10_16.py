def convert_length(value, unit):
    if unit == 'meters':
        return value
    elif unit == 'feet':
        return value * 3.28084
    elif unit == 'kilometers':
        return value / 1000.0
    else:
        raise ValueError("Unsupported unit: {}".format(unit))

if __name__ == '__main__':
    print(convert_length(1, 'meters'))
    print(convert_length(1, 'feet'))
    print(convert_length(1000, 'kilometers'))
    try:
        convert_length(1, 'miles')
    except ValueError as e:
        print(e)