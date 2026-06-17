import math
def convert_units_iterative(value, source_unit, target_unit):
    if source_unit == target_unit:
        return value
    conversion_factors = {
        ('m', 'km'): 1000.0,
        ('cm', 'm'): 0.01,
        ('m', 'cm'): 100.0,
        ('kg', 'g'): 1000.0,
        ('g', 'kg'): 0.001,
        ('L', 'm3'): 1000.0,
        ('m3', 'L'): 1000.0,
    }
    if (source_unit, target_unit) in conversion_factors:
        factor = conversion_factors[(source_unit, target_unit)]
        return value * factor
    else:
        raise ValueError(f"Conversion factor not defined for {source_unit} to {target_unit}")
if __name__ == '__main__':
    value1 = 5000.0
    source1 = 'm'
    target1 = 'km'
    try:
        result1 = convert_units_iterative(value1, source1, target1)
        print(f"Result 1: {value1} {source1} is {result1} {target1}")
    except ValueError as e:
        print(f"Error 1: {e}")
    value2 = 2500.0
    source2 = 'g'
    target2 = 'kg'
    try:
        result2 = convert_units_iterative(value2, source2, target2)
        print(f"Result 2: {value2} {source2} is {result2} {target2}")
    except ValueError as e:
        print(f"Error 2: {e}")
    value3 = 75.0
    source3 = 'cm'
    target3 = 'm'
    try:
        result3 = convert_units_iterative(value3, source3, target3)
        print(f"Result 3: {value3} {source3} is {result3} {target3}")
    except ValueError as e:
        print(f"Error 3: {e}")
    value4 = 10.0
    source4 = 'm'
    target4 = 'm'
    try:
        result4 = convert_units_iterative(value4, source4, target4)
        print(f"Result 4: {value4} {source4} is {result4} {target4}")
    except ValueError as e:
        print(f"Error 4: {e}")
    value5 = 1.5
    source5 = 'm'
    target5 = 'cm'
    try:
        result5 = convert_units_iterative(value5, source5, target5)
        print(f"Result 5: {value5} {source5} is {result5} {target5}")
    except ValueError as e:
        print(f"Error 5: {e}")