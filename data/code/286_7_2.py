import math
def convert_length(value, from_unit, to_unit):
    if from_unit == to_unit:
        return value
    if from_unit == "meters":
        if to_unit == "feet":
            return value * 3.28084
        elif to_unit == "miles":
            return value / 1609.34
    elif from_unit == "feet":
        if to_unit == "meters":
            return value / 3.28084
        elif to_unit == "miles":
            return value / 5280
    elif from_unit == "miles":
        if to_unit == "meters":
            return value * 1609.34
        elif to_unit == "feet":
            return value * 5280
    raise ValueError("Invalid unit specified")
if __name__ == '__main__':
    value = 10
    from_unit = "meters"
    to_unit_feet = "feet"
    to_unit_miles = "miles"
    result_feet = convert_length(value, from_unit, to_unit_feet)
    result_miles = convert_length(value, from_unit, to_unit_miles)
    print(f"{value} {from_unit} is equal to {result_feet:.4f} {to_unit_feet}")
    print(f"{value} {from_unit} is equal to {result_miles:.4f} {to_unit_miles}")
    value = 60
    from_unit = "feet"
    to_unit_meters = "meters"
    to_unit_miles_2 = "miles"
    result_meters = convert_length(value, from_unit, to_unit_meters)
    result_miles_2 = convert_length(value, from_unit, to_unit_miles_2)
    print(f"{value} {from_unit} is equal to {result_meters:.4f} {to_unit_meters}")
    print(f"{value} {from_unit} is equal to {result_miles_2:.4f} {to_unit_miles_2}")
    value = 1
    from_unit = "miles"
    to_unit_feet = "feet"
    result_feet_3 = convert_length(value, from_unit, to_unit_feet)
    print(f"{value} {from_unit} is equal to {result_feet_3:.4f} {to_unit_feet}")