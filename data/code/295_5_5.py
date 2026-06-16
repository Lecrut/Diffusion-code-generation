class UnitConversionError(Exception):
    pass
def convert_temperature(value, from_unit, to_unit):
    if not isinstance(value, (int, float)):
        raise TypeError("Input value must be numeric.")
    if not isinstance(from_unit, str) or not isinstance(to_unit, str):
        raise TypeError("Unit names must be strings.")
    if from_unit.lower() == to_unit.lower():
        return value
    if from_unit.lower() == "celsius" and to_unit.lower() == "fahrenheit":
        return (value * 9/5) + 32
    elif from_unit.lower() == "fahrenheit" and to_unit.lower() == "celsius":
        return (value - 32) * 5/9
    else:
        raise UnitConversionError(f"Unsupported temperature conversion: {from_unit} to {to_unit}")
def convert_length(value, from_unit, to_unit):
    if not isinstance(value, (int, float)):
        raise TypeError("Input value must be numeric.")
    if not isinstance(from_unit, str) or not isinstance(to_unit, str):
        raise TypeError("Unit names must be strings.")
    if from_unit.lower() == to_unit.lower():
        return value
    if from_unit.lower() == "meter" and to_unit.lower() == "kilometer":
        return value / 1000
    elif from_unit.lower() == "kilometer" and to_unit.lower() == "meter":
        return value * 1000
    else:
        raise UnitConversionError(f"Unsupported length conversion: {from_unit} to {to_unit}")
if __name__ == '__main__':
    print("--- Temperature Conversions ---")
    try:
        result1 = convert_temperature(25, "Celsius", "Fahrenheit")
        print(f"25 Celsius is {result1:.2f} Fahrenheit")
        result2 = convert_temperature(0, "Celsius", "Kelvin")
        print(f"0 Celsius to Kelvin: {result2}")
        result3 = convert_temperature(10, "Celsius", "Fahrenheit")
        print(f"10 Celsius is {result3:.2f} Fahrenheit")
        print("\n--- Length Conversions ---")
        result4 = convert_length(5, "meter", "kilometer")
        print(f"5 meter is {result4} kilometer")
        result5 = convert_length(2.5, "kilometer", "meter")
        print(f"2.5 kilometer is {result5} meter")
        try:
            convert_temperature(10, "Celsius", "Kelvin")
        except UnitConversionError as e:
            print(f"\nCaught expected error for unsupported temp conversion: {e}")
        try:
            convert_length(5, "meter", "mile")
        except UnitConversionError as e:
            print(f"Caught expected error for unsupported length conversion: {e}")
        try:
            convert_temperature("abc", "Celsius", "Fahrenheit")
        except TypeError as e:
            print(f"Caught expected error for non-numeric input: {e}")
    except Exception as e:
        print(f"An unexpected error occurred during testing: {e}")