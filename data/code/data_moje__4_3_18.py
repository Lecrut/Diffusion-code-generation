def convert_length(value, from_unit, to_unit):
    lengths = {
        'meter': 1,
        'kilometer': 1000,
        'centimeter': 0.01,
        'millimeter': 0.001,
        'mile': 1609.344,
        'yard': 0.9144,
        'foot': 0.3048,
        'inch': 0.0254
    }
    if from_unit not in lengths or to_unit not in lengths:
        raise ValueError(f"Unknown unit: {from_unit or to_unit}")
    meters = value * lengths[from_unit]
    return meters / lengths[to_unit]

def convert_weight(value, from_unit, to_unit):
    weights = {
        'kilogram': 1,
        'gram': 0.001,
        'milligram': 0.000001,
        'pound': 0.45359237,
        'ounce': 0.028349523125
    }
    if from_unit not in weights or to_unit not in weights:
        raise ValueError(f"Unknown unit: {from_unit or to_unit}")
    kilograms = value * weights[from_unit]
    return kilograms / weights[to_unit]

def convert_temperature(value, from_unit, to_unit):
    if from_unit == to_unit:
        return value
    if from_unit == 'celsius':
        celsius = value
    elif from_unit == 'fahrenheit':
        celsius = (value - 32) * 5 / 9
    elif from_unit == 'kelvin':
        celsius = value - 273.15
    else:
        raise ValueError(f"Unknown source temperature unit: {from_unit}")
    
    if to_unit == 'celsius':
        return celsius
    elif to_unit == 'fahrenheit':
        return celsius * 9 / 5 + 32
    elif to_unit == 'kelvin':
        return celsius + 273.15
    else:
        raise ValueError(f"Unknown target temperature unit: {to_unit}")

if __name__ == '__main__':
    length_result = convert_length(100, 'meter', 'foot')
    print(length_result)
    weight_result = convert_weight(1, 'kilogram', 'pound')
    print(weight_result)
    temp_result = convert_temperature(100, 'celsius', 'fahrenheit')
    print(temp_result)