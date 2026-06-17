import math
def convert_length(value, unit):
    if unit in ["m", "meter", "meters"]:
        if unit == "m":
            return value
        elif unit == "meter":
            return value
        elif unit == "meters":
            return value
    elif unit in ["km", "kilometer", "kilometers"]:
        if unit == "km":
            return value * 1000
        elif unit == "kilometer":
            return value * 1000
        elif unit == "kilometers":
            return value * 1000
    elif unit in ["ft", "foot", "feet"]:
        if unit == "ft":
            return value * 0.3048
        elif unit == "foot":
            return value * 0.3048
        elif unit == "feet":
            return value * 0.3048
    elif unit in ["mi", "mile", "miles"]:
        if unit == "mi":
            return value * 1609.34
        elif unit == "mile":
            return value * 1609.34
        elif unit == "miles":
            return value * 1609.34
    return None
def convert_mass(value, unit):
    if unit in ["g", "gram", "grams"]:
        if unit == "g":
            return value
        elif unit == "gram":
            return value
        elif unit == "grams":
            return value
    elif unit in ["kg", "kilogram", "kilograms"]:
        if unit == "kg":
            return value
        elif unit == "kilogram":
            return value
        elif unit == "kilograms":
            return value
    elif unit in ["lb", "pound", "pounds"]:
        if unit == "lb":
            return value * 0.453592
        elif unit == "pound":
            return value * 0.453592
        elif unit == "pounds":
            return value * 0.453592
    elif unit in ["oz", "ounce", "ounces"]:
        if unit == "oz":
            return value * 0.0283495
        elif unit == "ounce":
            return value * 0.0283495
        elif unit == "ounces":
            return value * 0.0283495
    return None
if __name__ == '__main__':
    sample_length = 10
    sample_length_unit = "m"
    sample_mass = 5
    sample_mass_unit = "kg"
    print("--- Length Conversion ---")
    converted_length_ft = convert_length(sample_length, sample_length_unit)
    if converted_length_ft is not None:
        print(f"{sample_length} {sample_length_unit} is equal to {converted_length_ft:.2f} feet")
    converted_length_mi = convert_length(sample_length, sample_length_unit)
    if converted_length_mi is not None:
        print(f"{sample_length} {sample_length_unit} is equal to {converted_length_mi:.2f} miles")
    print("\n--- Mass Conversion ---")
    converted_mass_lb = convert_mass(sample_mass, sample_mass_unit)
    if converted_mass_lb is not None:
        print(f"{sample_mass} {sample_mass_unit} is equal to {converted_mass_lb:.2f} pounds")
    converted_mass_oz = convert_mass(sample_mass, sample_mass_unit)
    if converted_mass_oz is not None:
        print(f"{sample_mass} {sample_mass_unit} is equal to {converted_mass_oz:.2f} ounces")