class UnitConversionError(Exception):
    pass
def convert_temperature(value, from_unit, to_unit):
    if not isinstance(value, (int, float)):
        raise UnitConversionError("Temperature value must be numeric.")
    if from_unit not in ["Celsius", "Fahrenheit", "Kelvin"] or to_unit not in ["Celsius", "Fahrenheit", "Kelvin"]:
        raise UnitConversionError("Unsupported temperature unit provided.")
    if from_unit == to_unit:
        return value
    celsius = None
    if from_unit == "Celsius":
        celsius = value
    elif from_unit == "Fahrenheit":
        celsius = (value - 32) * 5 / 9
    elif from_unit == "Kelvin":
        celsius = value - 273.15
    if celsius is None:
        raise UnitConversionError("Invalid source unit.")
    result = None
    if to_unit == "Celsius":
        result = celsius
    elif to_unit == "Fahrenheit":
        result = (celsius * 9 / 5) + 32
    elif to_unit == "Kelvin":
        result = celsius + 273.15
    else:
        raise UnitConversionError("Invalid target unit.")
    return result
def convert_mass(value, from_unit, to_unit):
    if not isinstance(value, (int, float)):
        raise UnitConversionError("Mass value must be numeric.")
    if from_unit not in ["kg", "g", "lb"] or to_unit not in ["kg", "g", "lb"]:
        raise UnitConversionError("Unsupported mass unit provided.")
    if from_unit == to_unit:
        return value
    to_kg = 0.0
    if from_unit == "kg":
        to_kg = value
    elif from_unit == "g":
        to_kg = value / 1000.0
    elif from_unit == "lb":
        to_kg = value * 0.453592
    result = None
    if to_unit == "kg":
        result = to_kg
    elif to_unit == "g":
        result = to_kg * 1000.0
    elif to_unit == "lb":
        result = to_kg / 0.453592
    else:
        raise UnitConversionError("Invalid target unit.")
    return result
if __name__ == '__main__':
    print("--- Temperature Conversion Tests ---")
    try:
        temp1 = convert_temperature(25, "Celsius", "Fahrenheit")
        print(f"25 Celsius is {temp1:.2f} Fahrenheit")
        temp2 = convert_temperature(300, "Kelvin", "Celsius")
        print(f"300 Kelvin is {temp2:.2f} Celsius")
        convert_temperature(10, "Celsius", "Rankine")
    except UnitConversionError as e:
        print(f"Error caught: {e}")
    print("\n--- Mass Conversion Tests ---")
    try:
        mass1 = convert_mass(500, "g", "kg")
        print(f"500 g is {mass1:.2f} kg")
        mass2 = convert_mass(10, "lb", "kg")
        print(f"10 lb is {mass2:.2f} kg")
        convert_mass(100, "ton", "kg")
    except UnitConversionError as e:
        print(f"Error caught: {e}")
    print("\n--- Error Handling Tests ---")
    try:
        convert_temperature("abc", "Celsius", "Fahrenheit")
    except UnitConversionError as e:
        print(f"Caught expected error for non-numeric input: {e}")
    try:
        convert_mass(10, "meter", "kg")
    except UnitConversionError as e:
        print(f"Caught expected error for unsupported unit: {e}")