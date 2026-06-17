import math
def convert_units(value, from_unit, to_unit):
    if from_unit == to_unit:
        return value
    if from_unit == "meter":
        if to_unit == "kilogram":
            raise ValueError("Cannot directly convert meters to kilograms without density information.")
        elif to_unit == "gram":
            return value * 1000
        elif to_unit == "pound_mass":
            return value * 2.2046226218
        elif to_unit == "ounce":
            return value * 35.27396195
    elif from_unit == "kilogram":
        if to_unit == "meter":
            raise ValueError("Cannot directly convert kilograms to meters without density information.")
        elif to_unit == "gram":
            return value * 1000
        elif to_unit == "pound_mass":
            return value / 0.45359237
        elif to_unit == "ounce":
            return value / 0.022046226218
    elif from_unit == "meter":
        if to_unit == "foot":
            return value / 0.3048
        elif to_unit == "inch":
            return value * 39.3701
    elif from_unit == "foot":
        if to_unit == "meter":
            return value * 0.3048
        elif to_unit == "inch":
            return value * 12
    elif from_unit == "inch":
        if to_unit == "foot":
            return value / 12
        elif to_unit == "meter":
            return value / 39.3701
    elif from_unit == "pound_mass":
        if to_unit == "kilogram":
            return value * 0.45359237
        elif to_unit == "gram":
            return value * 453.59237
        elif to_unit == "ounce":
            return value / 0.022046226218
    elif from_unit == "ounce":
        if to_unit == "pound_mass":
            return value * 0.022046226218
        elif to_unit == "gram":
            return value * 28.349523
    else:
        raise ValueError(f"Unknown unit: {from_unit}")
def chained_conversion(initial_value, from_unit, to_unit):
    if from_unit == to_unit:
        return initial_value
    if from_unit == "meter":
        intermediate_value = convert_units(initial_value, "meter", "meter")
        if to_unit in ["foot", "inch"]:
            return convert_units(intermediate_value, "meter", to_unit)
        elif to_unit in ["gram", "ounce"]:
            pass
    if from_unit == "kilogram":
        intermediate_value = convert_units(initial_value, "kilogram", "kilogram")
        if to_unit in ["gram", "ounce"]:
            return convert_units(intermediate_value, "kilogram", to_unit)
        elif to_unit == "meter":
            raise ValueError("Cannot chain mass conversion directly to length without density.")
    if from_unit != "meter" and to_unit in ["meter", "foot", "inch"]:
        return convert_units(initial_value, from_unit, to_unit)
    raise NotImplementedError(f"Chained conversion from {from_unit} to {to_unit} is not directly supported by this implementation.")
if __name__ == '__main__':
    print("--- Length Conversions (Meter based) ---")
    try:
        val1 = 10.0
        from1 = "meter"
        to1 = "foot"
        result1 = chained_conversion(val1, from1, to1)
        print(f"{val1} {from1} is {result1} {to1}")
        val2 = 60.0
        from2 = "foot"
        to2 = "meter"
        result2 = chained_conversion(val2, from2, to2)
        print(f"{val2} {from2} is {result2} {to2}")
        val3 = 30.0
        from3 = "inch"
        to3 = "foot"
        result3 = chained_conversion(val3, from3, to3)
        print(f"{val3} {from3} is {result3} {to3}")
    except (ValueError, NotImplementedError) as e:
        print(f"Error during length conversion: {e}")
    print("\n--- Mass Conversions (Kilogram/Pound based) ---")
    try:
        val4 = 10.0
        from4 = "kilogram"
        to4 = "pound_mass"
        result4 = chained_conversion(val4, from4, to4)
        print(f"{val4} {from4} is {result4} {to4}")
        val5 = 2.2046226218
        from5 = "pound_mass"
        to5 = "gram"
        result5 = chained_conversion(val5, from5, to5)
        print(f"{val5} {from5} is {result5} {to5}")
    except (ValueError, NotImplementedError) as e:
        print(f"Error during mass conversion: {e}")