class UnitConversionError(Exception):
    pass
def convert_temperature(value, from_unit, to_unit):
    if not isinstance(value, (int, float)):
        raise UnitConversionError("Input value must be numeric.")
    if from_unit not in ["Celsius", "Fahrenheit", "Kelvin"] or to_unit not in ["Celsius", "Fahrenheit", "Kelvin"]:
        raise UnitConversionError("Unsupported temperature unit provided.")
    if from_unit == to_unit:
        return value
    if from_unit == "Celsius":
        if to_unit == "Fahrenheit":
            return (value * 9/5) + 32
        elif to_unit == "Kelvin":
            return value + 273.15
    elif from_unit == "Fahrenheit":
        if to_unit == "Celsius":
            return (value - 32) * 5/9
        elif to_unit == "Kelvin":
            return (value - 32) * 5/9 + 273.15
    elif from_unit == "Kelvin":
        if to_unit == "Celsius":
            return value - 273.15
        elif to_unit == "Fahrenheit":
            return (value - 273.15) * 9/5 + 32
def convert_mass(value, from_unit, to_unit):
    if not isinstance(value, (int, float)):
        raise UnitConversionError("Input value must be numeric.")
    if from_unit not in ["kg", "g"] or to_unit not in ["kg", "g"]:
        raise UnitConversionError("Unsupported mass unit provided.")
    if from_unit == to_unit:
        return value
    if from_unit == "kg":
        if to_unit == "g":
            return value * 1000.0
    elif from_unit == "g":
        if to_unit == "kg":
            return value / 1000.0
def convert_length(value, from_unit, to_unit):
    if not isinstance(value, (int, float)):
        raise UnitConversionError("Input value must be numeric.")
    if from_unit not in ["m", "cm"] or to_unit not in ["m", "cm"]:
        raise UnitConversionError("Unsupported length unit provided.")
    if from_unit == to_unit:
        return value
    if from_unit == "m":
        if to_unit == "cm":
            return value * 100.0
    elif from_unit == "cm":
        if to_unit == "m":
            return value / 100.0
if __name__ == '__main__':
    print("--- Temperature Conversion Tests ---")
    try:
        result1 = convert_temperature(25, "Celsius", "Fahrenheit")
        print(f"25 Celsius to Fahrenheit: {result1}")
        result2 = convert_temperature(0, "Kelvin", "Celsius")
        print(f"0 Kelvin to Celsius: {result2}")
        result3 = convert_temperature(100, "Fahrenheit", "Celsius")
        print(f"100 Fahrenheit to Celsius: {result3}")
        print("\n--- Error Handling Tests (Temperature) ---")
        convert_temperature("abc", "Celsius", "Fahrenheit")
    except UnitConversionError as e:
        print(f"Caught expected error: {e}")
    except Exception as e:
        print(f"Caught unexpected error: {e}")
    print("\n--- Mass Conversion Tests ---")
    try:
        result4 = convert_mass(500, "g", "kg")
        print(f"500 g to kg: {result4}")
        result5 = convert_mass(2.5, "kg", "g")
        print(f"2.5 kg to g: {result5}")
        print("\n--- Error Handling Tests (Mass) ---")
        convert_mass("invalid", "kg", "g")
    except UnitConversionError as e:
        print(f"Caught expected error: {e}")
    except Exception as e:
        print(f"Caught unexpected error: {e}")
    print("\n--- Length Conversion Tests ---")
    try:
        result6 = convert_length(10, "m", "cm")
        print(f"10 m to cm: {result6}")
        result7 = convert_length(50, "cm", "m")
        print(f"50 cm to m: {result7}")
        print("\n--- Error Handling Tests (Length) ---")
        convert_length(10.5, "ft", "m")
    except UnitConversionError as e:
        print(f"Caught expected error: {e}")
    except Exception as e:
        print(f"Caught unexpected error: {e}")