UNIT_CONVERSIONS = {
    'meter': {'meter': 1.0, 'kilometer': 1000.0, 'centimeter': 100.0, 'millimeter': 1000.0, 'inch': 39.3701, 'foot': 3.28084, 'mile': 0.000621371},
    'kilogram': {'kilogram': 1.0, 'gram': 1000.0, 'pound': 2.20462, 'ounce': 35.274},
    'liter': {'liter': 1.0, 'milliliter': 1000.0, 'gallon': 0.264172, 'quart': 1.05669},
    'celsius': {'celsius': 1.0, 'fahrenheit': None, 'kelvin': None},
    'fahrenheit': {'celsius': None, 'fahrenheit': 1.0, 'kelvin': None},
    'kelvin': {'celsius': None, 'fahrenheit': None, 'kelvin': 1.0},
}

def convert_temperature(value, from_unit, to_unit):
    if from_unit == to_unit:
        return value
    if from_unit == 'celsius':
        celsius = value
    elif from_unit == 'fahrenheit':
        celsius = (value - 32) * 5.0 / 9.0
    elif from_unit == 'kelvin':
        celsius = value - 273.15
    else:
        raise ValueError(f"Unknown source temperature unit: {from_unit}")
    
    if to_unit == 'celsius':
        return celsius
    elif to_unit == 'fahrenheit':
        return (celsius * 9.0 / 5.0) + 32
    elif to_unit == 'kelvin':
        return celsius + 273.15
    else:
        raise ValueError(f"Unknown target temperature unit: {to_unit}")

def convert(value, from_unit, to_unit):
    if from_unit == to_unit:
        return value
    
    temp_units = {'celsius', 'fahrenheit', 'kelvin'}
    
    if from_unit in temp_units or to_unit in temp_units:
        if from_unit not in temp_units or to_unit not in temp_units:
            raise ValueError("Cannot convert between temperature and other units.")
        return convert_temperature(value, from_unit, to_unit)
    
    base = None
    if from_unit in UNIT_CONVERSIONS:
        base = 'meter' if 'meter' in UNIT_CONVERSIONS[from_unit] else 'kilogram' if 'kilogram' in UNIT_CONVERSIONS[from_unit] else 'liter'
        factors = UNIT_CONVERSIONS[from_unit]
    elif to_unit in UNIT_CONVERSIONS:
        base = 'meter' if 'meter' in UNIT_CONVERSIONS[to_unit] else 'kilogram' if 'kilogram' in UNIT_CONVERSIONS[to_unit] else 'liter'
        factors = UNIT_CONVERSIONS[to_unit]
    else:
        raise ValueError(f"Unknown unit: {from_unit} or {to_unit}")
        
    if base == 'meter':
        units_map = 'meter'
    elif base == 'kilogram':
        units_map = 'kilogram'
    else:
        units_map = 'liter'
        
    if from_unit not in UNIT_CONVERSIONS or to_unit not in UNIT_CONVERSIONS[from_unit]:
         raise ValueError(f"Conversion not supported for {from_unit} to {to_unit}")

    from_factor = UNIT_CONVERSIONS[units_map].get(from_unit, None)
    to_factor = UNIT_CONVERSIONS[units_map].get(to_unit, None)

    if from_factor is None or to_factor is None:
        raise ValueError(f"Invalid unit mapping for {from_unit} or {to_unit}")

    base_value = value * from_factor
    return base_value / to_factor

if __name__ == '__main__':
    result_km = convert(1, 'meter', 'kilometer')
    result_inches = convert(1, 'meter', 'inch')
    result_f = convert(100, 'celsius', 'fahrenheit')
    result_kg = convert(1, 'kilogram', 'pound')
    
    print(result_km)
    print(result_inches)
    print(result_f)
    print(result_kg)