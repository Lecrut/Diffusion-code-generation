def convert_length(value, unit):
    if unit == 'meters':
        return value
    if unit == 'feet':
        return value * 0.3048
    if unit == 'kilometers':
        return value * 1000
    raise ValueError(f"Unsupported unit: {unit}")

if __name__ == '__main__':
    result = convert_length(100, 'feet')
    print(result)
    result2 = convert_length(1, 'kilometers')
    print(result2)
    result3 = convert_length(5, 'meters')
    print(result3)
    try:
        convert_length(10, 'yards')
    except ValueError as e:
        print(e)