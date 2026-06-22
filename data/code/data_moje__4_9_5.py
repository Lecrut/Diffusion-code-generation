def convert_distance(value, from_unit, to_unit):
    if from_unit == "miles" and to_unit == "kilometers":
        return value * 1.60934
    elif from_unit == "kilometers" and to_unit == "miles":
        return value / 1.60934
    else:
        if from_unit == to_unit:
            return value
        raise ValueError("Unsupported unit conversion")

if __name__ == '__main__':
    result = convert_distance(10, "miles", "kilometers")
    print(result)