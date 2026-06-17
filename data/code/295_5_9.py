class UnitConversionError(Exception):
    pass
def convert_temperature(value, from_unit, to_unit):
    if not isinstance(value, (int, float)):
        raise TypeError("Input value must be numeric.")
    if not isinstance(from_unit, str) or not isinstance(to_unit, str):
        raise TypeError("Unit inputs must be strings.")
    if from_unit.lower() == to_unit.lower():
        return value
    if from_unit.lower() == 'c' and to_unit.lower() == 'f':
        return (value * 9/5) + 32
    elif from_unit.lower() == 'f' and to_unit.lower() == 'c':
        return (value - 32) * 5/9
    else:
        raise UnitConversionError(f"Unsupported temperature conversion from {from_unit} to {to_unit}")
def convert_mass(value, from_unit, to_unit):
    if not isinstance(value, (int, float)):
        raise TypeError("Input value must be numeric.")
    if not isinstance(from_unit, str) or not isinstance(to_unit, str):
        raise TypeError("Unit inputs must be strings.")
    if from_unit.lower() == to_unit.lower():
        return value
    if from_unit.lower() == 'kg' and to_unit.lower() == 'lb':
        return value * 2.20462
    elif from_unit.lower() == 'lb' and to_unit.lower() == 'kg':
        return value / 2.20462
    else:
        raise UnitConversionError(f"Unsupported mass conversion from {from_unit} to {to_unit}")
if __name__ == '__main__':
    print("--- Temperature Conversions ---")
    try:
        temp1 = convert_temperature(20, 'c', 'f')
        print(f"20 C is {temp1:.2f} F")
        temp2 = convert_temperature(32, 'f', 'c')
        print(f"32 F is {temp2:.2f} C")
        convert_temperature(10, 'c', 'k')
    except (TypeError, UnitConversionError) as e:
        print(f"Error during temperature conversion: {e}")
    print("\n--- Mass Conversions ---")
    try:
        mass1 = convert_mass(10, 'kg', 'lb')
        print(f"10 kg is {mass1:.2f} lb")
        mass2 = convert_mass(5, 'lb', 'kg')
        print(f"5 lb is {mass2:.2f} kg")
        convert_mass(10, 'g', 'kg')
    except (TypeError, UnitConversionError) as e:
        print(f"Error during mass conversion: {e}")
    print("\n--- Error Handling Tests ---")
    try:
        convert_temperature("twenty", 'c', 'f')
    except (TypeError, UnitConversionError) as e:
        print(f"Caught expected error for temperature type: {e}")
    try:
        convert_mass(10, 'kg', 'ton')
    except (TypeError, UnitConversionError) as e:
        print(f"Caught expected error for unsupported mass unit: {e}")