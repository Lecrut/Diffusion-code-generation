def convert_distance(value, from_unit, to_unit):
    if from_unit == to_unit:
        return value
    if from_unit == "m" and to_unit == "km":
        return value / 1000
    elif from_unit == "km" and to_unit == "m":
        return value * 1000
    elif from_unit == "ft" and to_unit == "in":
        return value * 12
    elif from_unit == "in" and to_unit == "ft":
        return value / 12
    else:
        raise ValueError("Unsupported unit conversion")
if __name__ == '__main__':
    value = 10
    from_unit = "m"
    to_unit = "km"
    result = convert_distance(value, from_unit, to_unit)
    print(result)
    value = 12
    from_unit = "ft"
    to_unit = "in"
    result = convert_distance(value, from_unit, to_unit)
    print(result)