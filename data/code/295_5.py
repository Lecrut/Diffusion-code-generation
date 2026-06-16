class UnitConversionError(Exception):
    pass
def convert_temperature(value, from_unit, to_unit):
    if not isinstance(value, (int, float)):
        raise TypeError("Temperature value must be numeric.")
    if from_unit not in ['Celsius', 'Fahrenheit', 'Kelvin'] or to_unit not in ['Celsius', 'Fahrenheit', 'Kelvin']:
        raise UnitConversionError("Unsupported temperature unit provided.")
    if from_unit == to_unit:
        return value
    if from_unit == 'Celsius':
        base_temp = value
    elif from_unit == 'Fahrenheit':
        base_temp = (value - 32) * 5 / 9
    elif from_unit == 'Kelvin':
        base_temp = value - 273.15
    else:
        raise UnitConversionError(f"Unknown source unit: {from_unit}")
    if to_unit == 'Celsius':
        result = base_temp
    elif to_unit == 'Fahrenheit':
        result = (base_temp * 9 / 5) + 32
    elif to_unit == 'Kelvin':
        result = base_temp + 273.15
    else:
        raise UnitConversionError(f"Unknown target unit: {to_unit}")
    return result
def convert_length(value, from_unit, to_unit):
    if not isinstance(value, (int, float)):
        raise TypeError("Length value must be numeric.")
    if from_unit not in ['meter', 'kilometer', 'mile'] or to_unit not in ['meter', 'kilometer', 'mile']:
        raise UnitConversionError("Unsupported length unit provided.")
    CONVERSION_FACTORS = {
        'meter': 1.0,
        'kilometer': 1000.0,
        'mile': 1609.34
    }
    if from_unit == 'meter':
        base_length = value
    elif from_unit == 'kilometer':
        base_length = value * 1000.0
    elif from_unit == 'mile':
        base_length = value * 1609.34
    else:
        raise UnitConversionError(f"Unknown source length unit: {from_unit}")
    if to_unit == 'meter':
        result = base_length
    elif to_unit == 'kilometer':
        result = base_length / 1000.0
    elif to_unit == 'mile':
        result = base_length / 1609.34
    else:
        raise UnitConversionError(f"Unknown target length unit: {to_unit}")
    return result
if __name__ == '__main__':
    print("--- Temperature Conversions ---")
    try:
        temp1 = convert_temperature(25, 'Celsius', 'Fahrenheit')
        print(f"25 Celsius is {temp1:.2f} Fahrenheit")
        temp2 = convert_temperature(300, 'Kelvin', 'Celsius')
        print(f"300 Kelvin is {temp2:.2f} Celsius")
        convert_temperature(10, 'Celsius', 'Rankine')
    except (TypeError, UnitConversionError) as e:
        print(f"Error during temperature conversion: {e}")
    print("\n--- Length Conversions ---")
    try:
        length1 = convert_length(5, 'meter', 'kilometer')
        print(f"5 meter is {length1:.3f} kilometer")
        length2 = convert_length(10, 'mile', 'meter')
        print(f"10 mile is {length2:.2f} meter")
        convert_length(10.5, 'foot', 'meter')
    except (TypeError, UnitConversionError) as e:
        print(f"Error during length conversion: {e}")
    print("\n--- Error Handling Tests ---")
    try:
        convert_temperature("twenty", 'Celsius', 'Fahrenheit')
    except (TypeError, UnitConversionError) as e:
        print(f"Caught expected error for non-numeric input: {e}")
    try:
        convert_length(10, 'foot', 'meter')
    except (TypeError, UnitConversionError) as e:
        print(f"Caught expected error for unsupported unit: {e}")