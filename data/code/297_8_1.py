import math
def convert_unit_iterative(value, source_unit, target_unit):
    if source_unit == target_unit:
        return value
    conversion_factors = {
        ('m', 'cm'): 100.0,
        ('kg', 'g'): 1000.0,
        ('km', 'm'): 1000.0,
        ('L', 'm3'): 1000.0,
        ('in', 'cm'): 2.54,
        ('ft', 'm'): 0.3048,
        ('mi', 'km'): 1.60934,
    }
    if (source_unit, target_unit) in conversion_factors:
        factor = conversion_factors[(source_unit, target_unit)]
        result = value * factor
        return result
    else:
        raise ValueError(f"Conversion factor not defined for {source_unit} to {target_unit}")
if __name__ == '__main__':
    value = 10
    source = 'km'
    target = 'm'
    result = None
    try:
        result = convert_unit_iterative(value, source, target)
        print(f"Value: {value} {source}")
        print(f"Converted to: {result} {target}")
    except ValueError as e:
        print(f"Error: {e}")
    value = 500
    source = 'kg'
    target = 'g'
    result = None
    try:
        result = convert_unit_iterative(value, source, target)
        print(f"Value: {value} {source}")
        print(f"Converted to: {result} {target}")
    except ValueError as e:
        print(f"Error: {e}")
    value = 100
    source = 'in'
    target = 'cm'
    result = None
    try:
        result = convert_unit_iterative(value, source, target)
        print(f"Value: {value} {source}")
        print(f"Converted to: {result} {target}")
    except ValueError as e:
        print(f"Error: {e}")