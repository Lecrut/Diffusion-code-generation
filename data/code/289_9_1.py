def convert_distance(value, from_unit, to_unit):
    if from_unit == to_unit:
        return value
    if from_unit == "m" and to_unit == "km":
        return value / 1000
    elif from_unit == "km" and to_unit == "m":
        return value * 1000
    elif from_unit == "cm" and to_unit == "m":
        return value / 100
    elif from_unit == "m" and to_unit == "cm":
        return value * 100
    else:
        raise ValueError("Unsupported unit conversion")
if __name__ == '__main__':
    value = 5.2
    from_unit = "km"
    to_unit = "m"
    result = convert_distance(value, from_unit, to_unit)
    print(result)