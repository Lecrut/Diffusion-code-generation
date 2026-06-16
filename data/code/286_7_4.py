def convert_length(value, from_unit, to_unit):
    if from_unit == to_unit:
        return value
    meters = 0
    if from_unit == "meters":
        meters = value
    elif from_unit == "feet":
        meters = value * 0.3048
    elif from_unit == "miles":
        meters = value * 1609.34
    else:
        raise ValueError("Unsupported 'from_unit'")
    if to_unit == "meters":
        return meters
    elif to_unit == "feet":
        return meters / 0.3048
    elif to_unit == "miles":
        return meters / 1609.34
    else:
        raise ValueError("Unsupported 'to_unit'")
if __name__ == '__main__':
    print(convert_length(10, "meters", "feet"))
    print(convert_length(10, "feet", "meters"))
    print(convert_length(1, "miles", "meters"))
    print(convert_length(5, "meters", "miles"))
    print(convert_length(10, "feet", "miles"))
    print(convert_length(10, "meters", "meters"))