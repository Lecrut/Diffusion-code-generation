def convert_distance(distance, from_unit, to_unit):
    conversion_factors = {
        ('meter', 'meter'): 1.0,
        ('meter', 'kilometer'): 0.001,
        ('meter', 'centimeter'): 100.0,
        ('meter', 'millimeter'): 1000.0,
        ('meter', 'mile'): 0.000621371,
        ('meter', 'yard'): 1.09361,
        ('meter', 'foot'): 3.28084,
        ('meter', 'inch'): 39.3701,
        ('kilometer', 'meter'): 1000.0,
        ('kilometer', 'kilometer'): 1.0,
        ('kilometer', 'centimeter'): 100000.0,
        ('kilometer', 'millimeter'): 1000000.0,
        ('kilometer', 'mile'): 0.621371,
        ('kilometer', 'yard'): 1093.61,
        ('kilometer', 'foot'): 3280.84,
        ('kilometer', 'inch'): 39370.1,
        ('centimeter', 'meter'): 0.01,
        ('centimeter', 'kilometer'): 0.00001,
        ('centimeter', 'centimeter'): 1.0,
        ('centimeter', 'millimeter'): 10.0,
        ('centimeter', 'mile'): 0.00000621371,
        ('centimeter', 'yard'): 0.0109361,
        ('centimeter', 'foot'): 0.0328084,
        ('centimeter', 'inch'): 0.393701,
        ('millimeter', 'meter'): 0.001,
        ('millimeter', 'kilometer'): 0.000001,
        ('millimeter', 'centimeter'): 0.1,
        ('millimeter', 'millimeter'): 1.0,
        ('millimeter', 'mile'): 0.000000621371,
        ('millimeter', 'yard'): 0.00109361,
        ('millimeter', 'foot'): 0.00328084,
        ('millimeter', 'inch'): 0.0393701,
        ('mile', 'meter'): 1609.34,
        ('mile', 'kilometer'): 1.60934,
        ('mile', 'centimeter'): 160934.0,
        ('mile', 'millimeter'): 1609340.0,
        ('mile', 'mile'): 1.0,
        ('mile', 'yard'): 1760.0,
        ('mile', 'foot'): 5280.0,
        ('mile', 'inch'): 63360.0,
        ('yard', 'meter'): 0.9144,
        ('yard', 'kilometer'): 0.0009144,
        ('yard', 'centimeter'): 91.44,
        ('yard', 'millimeter'): 914.4,
        ('yard', 'mile'): 0.000568182,
        ('yard', 'yard'): 1.0,
        ('yard', 'foot'): 3.0,
        ('yard', 'inch'): 36.0,
        ('foot', 'meter'): 0.3048,
        ('foot', 'kilometer'): 0.0003048,
        ('foot', 'centimeter'): 30.48,
        ('foot', 'millimeter'): 304.8,
        ('foot', 'mile'): 0.000189394,
        ('foot', 'yard'): 0.333333,
        ('foot', 'foot'): 1.0,
        ('foot', 'inch'): 12.0,
        ('inch', 'meter'): 0.0254,
        ('inch', 'kilometer'): 0.0000254,
        ('inch', 'centimeter'): 2.54,
        ('inch', 'millimeter'): 25.4,
        ('inch', 'mile'): 0.0000157828,
        ('inch', 'yard'): 0.0277778,
        ('inch', 'foot'): 0.0833333,
        ('inch', 'inch'): 1.0
    }

    key = (from_unit.lower(), to_unit.lower())
    if key not in conversion_factors:
        raise ValueError(f"Unsupported unit conversion: {from_unit} to {to_unit}")

    factor = conversion_factors[key]
    if factor == 0.0:
        raise ZeroDivisionError("Division by zero in conversion factor")

    return distance * factor

if __name__ == '__main__':
    print(convert_distance(1, 'meter', 'kilometer'))
    print(convert_distance(100, 'centimeter', 'inch'))
    print(convert_distance(5.5, 'mile', 'meter'))
    print(convert_distance(0, 'foot', 'yard'))