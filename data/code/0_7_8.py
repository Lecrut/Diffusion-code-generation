import math
def convert_units(value, from_unit, to_unit, conversion_factors):
    if from_unit == to_unit:
        return value
    if from_unit not in conversion_factors or to_unit not in conversion_factors:
        raise ValueError("One or both units not found in conversion factors.")
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
    value1 = 5
    from_unit1 = "km"
    to_unit1 = "m"
    result1 = convert_units(value1, from_unit1, to_unit1, conversion_factors)
    print(f"{value1} {from_unit1} is equal to {result1} {BASE_UNIT}")
    value2 = 1000
    from_unit2 = "m"
    to_unit2 = "cm"
    result2 = convert_units(value2, from_unit2, to_unit2, conversion_factors)
    print(f"{value2} {from_unit2} is equal to {result2} {to_unit2}")
    value3 = 10
    from_unit3 = "ft"
    to_unit3 = "km"
    result3 = convert_units(value3, from_unit3, to_unit3, conversion_factors)
    print(f"{value3} {from_unit3} is equal to {result3} {to_unit3}")
    value4 = 500
    from_unit4 = "mm"
    to_unit4 = "m"
    result4 = convert_units(value4, from_unit4, to_unit4, conversion_factors)
    print(f"{value4} {from_unit4} is equal to {result4} {BASE_UNIT}")
    value5 = 1
    from_unit5 = "mi"
    to_unit5 = "ft"
    result5 = convert_units(value5, from_unit5, to_unit5, conversion_factors)
    print(f"{value5} {from_unit5} is equal to {result5} {to_unit5}")