class UnitConversionError(Exception):
    pass
def convert_temperature(value, from_unit, to_unit):
    if not isinstance(value, (int, float)):
        raise UnitConversionError("Temperature value must be numeric.")
    if from_unit not in ["C", "F", "K"] or to_unit not in ["C", "F", "K"]:
        raise UnitConversionError("Unsupported temperature unit provided.")
    if from_unit == to_unit:
        return value
    if from_unit == "C" and to_unit == "F":
        return (value * 9/5) + 32
    elif from_unit == "F" and to_unit == "C":
        return (value - 32) * 5/9
    elif from_unit == "C" and to_unit == "K":
        return value + 273.15
    elif from_unit == "K" and to_unit == "C":
        return value - 273.15
    elif from_unit == "F" and to_unit == "K":
        return (value + 459.67) * 5/9
    elif from_unit == "K" and to_unit == "F":
        return (value - 273.15) * 9/5 + 32
    else:
        raise UnitConversionError("Invalid temperature conversion path.")
def convert_length(value, from_unit, to_unit):
    if not isinstance(value, (int, float)):
        raise UnitConversionError("Length value must be numeric.")
    if from_unit not in ["m", "km", "mi"] or to_unit not in ["m", "km", "mi"]:
        raise UnitConversionError("Unsupported length unit provided.")
    if from_unit == to_unit:
        return value
    m_to_km = 1000.0
    m_to_mi = 0.000621371
    if from_unit == "m":
        if to_unit == "km":
            return value / m_to_km
        elif to_unit == "mi":
            return value * m_to_mi
    elif from_unit == "km":
        if to_unit == "m":
            return value * m_to_km
        elif to_unit == "mi":
            return value / m_to_mi
    elif from_unit == "mi":
        if to_unit == "m":
            return value / m_to_mi
        elif to_unit == "km":
            return value * m_to_km
    else:
        raise UnitConversionError("Invalid length conversion path.")
if __name__ == '__main__':
    print("--- Temperature Conversions ---")
    try:
        result1 = convert_temperature(25, "C", "F")
        print(f"25 C is {result1:.2f} F")
        result2 = convert_temperature(0, "K", "C")
        print(f"0 K is {result2:.2f} C")
        result3 = convert_temperature(100, "F", "C")
        print(f"100 F is {result3:.2f} C")
        convert_temperature("abc", "C", "F")
    except UnitConversionError as e:
        print(f"Error caught: {e}")
    print("\n--- Length Conversions ---")
    try:
        result4 = convert_length(5, "km", "m")
        print(f"5 km is {result4:.2f} m")
        result5 = convert_length(10, "mi", "km")
        print(f"10 mi is {result5:.2f} km")
        convert_length(10.5, "m", "mi")
        convert_length(10, "m", "lightyears")
    except UnitConversionError as e:
        print(f"Error caught: {e}")