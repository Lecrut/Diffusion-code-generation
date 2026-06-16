class UnitConversionError(Exception):
    pass
def convert_temperature(value, from_unit, to_unit):
    if not isinstance(value, (int, float)):
        raise TypeError("Input value must be numeric.")
    if from_unit not in ['Celsius', 'Fahrenheit', 'Kelvin'] or to_unit not in ['Celsius', 'Fahrenheit', 'Kelvin']:
        raise UnitConversionError("Unsupported temperature unit provided.")
    if from_unit == to_unit:
        return value
    if from_unit == 'Celsius':
        if to_unit == 'Fahrenheit':
            return (value * 9/5) + 32
        elif to_unit == 'Kelvin':
            return value + 273.15
    elif from_unit == 'Fahrenheit':
        if to_unit == 'Celsius':
            return (value - 32) * 5/9
        elif to_unit == 'Kelvin':
            return (value - 32) * 5/9 + 273.15
    elif from_unit == 'Kelvin':
        if to_unit == 'Celsius':
            return value - 273.15
        elif to_unit == 'Fahrenheit':
            return (value - 273.15) * 9/5 + 32
def convert_length(value, from_unit, to_unit):
    if not isinstance(value, (int, float)):
        raise TypeError("Input value must be numeric.")
    if from_unit not in ['meter', 'kilometer', 'mile'] or to_unit not in ['meter', 'kilometer', 'mile']:
        raise UnitConversionError("Unsupported length unit provided.")
    if from_unit == to_unit:
        return value
    if from_unit == 'meter':
        if to_unit == 'kilometer':
            return value / 1000
        elif to_unit == 'mile':
            return value / 1609.34
    elif from_unit == 'kilometer':
        if to_unit == 'meter':
            return value * 1000
        elif to_unit == 'mile':
            return value * 0.621371
    elif from_unit == 'mile':
        if to_unit == 'meter':
            return value * 1609.34
        elif to_unit == 'kilometer':
            return value / 0.621371
def main():
    print("--- Temperature Conversion Tests ---")
    try:
        result1 = convert_temperature(25, 'Celsius', 'Fahrenheit')
        print(f"25 Celsius to Fahrenheit: {result1}")
        result2 = convert_temperature(0, 'Kelvin', 'Celsius')
        print(f"0 Kelvin to Celsius: {result2}")
        result3 = convert_temperature(100, 'Celsius', 'Celsius')
        print(f"100 Celsius to Celsius: {result3}")
        result4 = convert_temperature(50, 'Celsius', 'MarsUnit')
    except (TypeError, UnitConversionError) as e:
        print(f"Caught Error in Temperature Test: {e}")
    print("\n--- Length Conversion Tests ---")
    try:
        result5 = convert_length(1000, 'meter', 'kilometer')
        print(f"1000 meter to kilometer: {result5}")
        result6 = convert_length(1, 'mile', 'meter')
        print(f"1 mile to meter: {result6}")
        result7 = convert_length(5, 'meter', 'lightyear')
    except (TypeError, UnitConversionError) as e:
        print(f"Caught Error in Length Test: {e}")
    print("\n--- Error Handling Tests ---")
    try:
        convert_temperature("abc", 'Celsius', 'Fahrenheit')
    except (TypeError, UnitConversionError) as e:
        print(f"Successfully caught expected error for non-numeric input: {e}")
    try:
        convert_length(10, 'meter', 'lightyear')
    except (TypeError, UnitConversionError) as e:
        print(f"Successfully caught expected error for unsupported unit: {e}")
if __name__ == '__main__':
    main()