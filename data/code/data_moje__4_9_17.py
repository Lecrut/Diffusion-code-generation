def convert_distance(value, unit):
    if unit == 'miles':
        return value * 1.609344
    if unit == 'kilometers':
        return value * 0.621371
    raise ValueError(f"Unsupported unit: {unit}")

if __name__ == '__main__':
    print(convert_distance(1, 'miles'))
    print(convert_distance(1, 'kilometers'))