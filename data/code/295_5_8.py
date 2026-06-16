class UnitConversionError(Exception):
    pass
def convert_temperature(value, from_unit, to_unit):
    if not isinstance(value, (int, float)):
        raise UnitConversionError("Temperature value must be numeric.")
    if from_unit == "C" and to_unit == "F":
        return (value * 9/5) + 32
    elif from_unit == "F" and to_unit == "C":
        return (value - 32) * 5/9
    else:
        raise UnitConversionError(f"Unsupported temperature conversion: {from_unit} to {to_unit}")
def convert_length(value, from_unit, to_unit):
    if not isinstance(value, (int, float)):
        raise UnitConversionError("Length value must be numeric.")
    if from_unit == "m" and to_unit == "km":
        return value / 1000
    elif from_unit == "km" and to_unit == "m":
        return value * 1000
    else:
        raise UnitConversionError(f"Unsupported length conversion: {from_unit} to {to_unit}")
if __name__ == '__main__':
    print("--- Testing Temperature Conversion ---")
    try:
        result_c_to_f = convert_temperature(20, "C", "F")
        print(f"20 C is {result_c_to_f:.2f} F")
        result_f_to_c = convert_temperature(68, "F", "C")
        print(f"68 F is {result_f_to_c:.2f} C")
        convert_temperature(10, "C", "K")
    except UnitConversionError as e:
        print(f"Caught Error: {e}")
    print("\n--- Testing Length Conversion ---")
    try:
        result_m_to_km = convert_length(5000, "m", "km")
        print(f"5000 m is {result_m_to_km:.2f} km")
        result_km_to_m = convert_length(10, "km", "m")
        print(f"10 km is {result_km_to_m:.2f} m")
        convert_length(100, "m", "cm")
    except UnitConversionError as e:
        print(f"Caught Error: {e}")
    print("\n--- Testing Error Handling (Non-numeric input) ---")
    try:
        convert_temperature("twenty", "C", "F")
    except UnitConversionError as e:
        print(f"Successfully caught error for non-numeric input: {e}")
    print("\n--- Testing Error Handling (Unsupported unit type) ---")
    try:
        convert_temperature(10, "C", "K")
    except UnitConversionError as e:
        print(f"Successfully caught error for unsupported conversion: {e}")
    try:
        convert_length(10, "m", "ft")
    except UnitConversionError as e:
        print(f"Successfully caught error for unsupported conversion: {e}")