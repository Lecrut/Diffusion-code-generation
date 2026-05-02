import math
def convert_length(value, from_unit, to_unit):
    if from_unit == to_unit:
        return value
    if from_unit == "m":
        if to_unit == "cm":
            return value * 100
        elif to_unit == "km":
            return value / 1000
        elif to_unit == "mm":
            return value * 1000
    elif from_unit == "cm":
        if to_unit == "m":
            return value / 100
        elif to_unit == "mm":
            return value * 10
    elif from_unit == "km":
        if to_unit == "m":
            return value * 1000
        elif to_unit == "cm":
            return value * 100000
        elif to_unit == "mm":
            return value * 1000000
    raise ValueError("Unsupported unit conversion")
if __name__ == '__main__':
    length = 10
    from_unit = "m"
    to_unit = "cm"
    result = convert_length(length, from_unit, to_unit)
    print(f"{length} {from_unit} is {result} {to_unit}")
    length = 5
    from_unit = "km"
    to_unit = "m"
    result = convert_length(length, from_unit, to_unit)
    print(f"{length} {from_unit} is {result} {to_unit}")
    length = 20
    from_unit = "cm"
    to_unit = "mm"
    result = convert_length(length, from_unit, to_unit)
    print(f"{length} {from_unit} is {result} {to_unit}")
    length = 10
    from_unit = "m"
    to_unit = "m"
    result = convert_length(length, from_unit, to_unit)
    print(f"{length} {from_unit} is {result} {to_unit}")