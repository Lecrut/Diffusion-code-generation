def convert_length(length, unit):
    supported_units = {
        "meters": 1.0,
        "feet": 0.3048,
        "kilometers": 1000.0,
    }

    if unit not in supported_units:
        raise ValueError(f"Unsupported unit: {unit}")

    meters = length * supported_units[unit]
    return meters

if __name__ == '__main__':
    result = convert_length(10, "feet")
    print(result)

    result2 = convert_length(1, "kilometers")
    print(result2)

    try:
        convert_length(5, "inches")
    except ValueError as e:
        print(e)