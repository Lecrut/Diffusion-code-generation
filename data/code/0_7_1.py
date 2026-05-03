import math
def convert_units(value, from_unit, to_unit, conversion_factors):
    if from_unit == to_unit:
        return value
    if from_unit not in conversion_factors or to_unit not in conversion_factors:
        raise ValueError("One or both units are not defined in the conversion factors.")
    value_in_base = value * conversion_factors[from_unit]
    value_in_target = value_in_base / conversion_factors[to_unit]
    return value_in_target
if __name__ == '__main__':
    BASE_UNIT = "m"
    conversion_factors = {
        "m": 1.0,                                  
        "km": 1000.0,                     
        "cm": 0.01,                       
        "mm": 0.001,                       
        "mi": 1609.34,                         
        "ft": 0.3048                          
    }
    value = 5.0
    from_unit = "km"
    to_unit = "m"
    result1 = convert_units(value, from_unit, to_unit, conversion_factors)
    print(f"{value} {from_unit} is equal to {result1} {BASE_UNIT}")
    value = 100.0
    from_unit = "cm"
    to_unit = "mm"
    result2 = convert_units(value, from_unit, to_unit, conversion_factors)
    print(f"{value} {from_unit} is equal to {result2} {to_unit}")
    value = 1.0
    from_unit = "mi"
    to_unit = "ft"
    result3 = convert_units(value, from_unit, to_unit, conversion_factors)
    print(f"{value} {from_unit} is equal to {result3} {to_unit}")
    value = 2.5
    from_unit = "ft"
    to_unit = "km"
    result4 = convert_units(value, from_unit, to_unit, conversion_factors)
    print(f"{value} {from_unit} is equal to {result4} {to_unit}")