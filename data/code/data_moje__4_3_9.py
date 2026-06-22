def kilometers_to_miles(km):
    return km * 0.621371

def miles_to_kilometers(mi):
    return mi / 0.621371

def meters_to_feet(m):
    return m * 3.28084

def feet_to_meters(ft):
    return ft / 3.28084

def centimeters_to_inches(cm):
    return cm * 0.393701

def inches_to_centimeters(inches):
    return inches / 0.393701

def kilometers_to_feet(km):
    return meters_to_feet(km * 1000)

def feet_to_kilometers(ft):
    return kilometers_to_miles(ft_to_meters(ft))

def celsius_to_fahrenheit(c):
    return (c * 9/5) + 32

def fahrenheit_to_celsius(f):
    return (f - 32) * 5/9

def kilograms_to_pounds(kg):
    return kg * 2.20462

def pounds_to_kilograms(lbs):
    return lbs / 2.20462

def grams_to_ounces(g):
    return g * 0.035274

def ounces_to_grams(oz):
    return oz / 0.035274

def liters_to_gallons(liters):
    return liters * 0.264172

def gallons_to_liters(gallons):
    return gallons / 0.264172

def milliliters_to_fluid_ounces(ml):
    return ml * 0.033814

def fluid_ounces_to_milliliters(floz):
    return floz / 0.033814

def convert_distance(value, from_unit, to_unit):
    unit_map = {
        'km': 0,
        'mi': 1,
        'm': 2,
        'ft': 3
    }
    
    conversions = {
        (0, 1): kilometers_to_miles,
        (1, 0): miles_to_kilometers,
        (2, 3): meters_to_feet,
        (3, 2): feet_to_meters,
        (0, 3): kilometers_to_feet,
        (3, 0): feet_to_kilometers
    }
    
    from_idx = unit_map.get(from_unit)
    to_idx = unit_map.get(to_unit)
    
    if from_idx is None or to_idx is None:
        raise ValueError(f"Unsupported units: {from_unit}, {to_unit}")
    
    if from_idx == to_idx:
        return value
    
    if (from_idx, to_idx) in conversions:
        return conversions[(from_idx, to_idx)](value)
    
    if from_idx in [0, 1]:
        if to_idx == 2:
            if from_idx == 0:
                return value * 1000
            else:
                return miles_to_kilometers(value) * 1000
        elif to_idx == 3:
            if from_idx == 0:
                return kilometers_to_feet(value)
            else:
                return feet_to_meters(miles_to_kilometers(value) * 1000)
    elif from_idx in [2, 3]:
        if to_idx == 0:
            if from_idx == 2:
                return value / 1000
            else:
                return feet_to_kilometers(value)
        elif to_idx == 1:
            if from_idx == 2:
                return kilometers_to_miles(value / 1000)
            else:
                return miles_to_kilometers(feet_to_kilometers(value))
    
    raise ValueError(f"No conversion path from {from_unit} to {to_unit}")

def convert_weight(value, from_unit, to_unit):
    unit_map = {
        'kg': 0,
        'lbs': 1,
        'g': 2,
        'oz': 3
    }
    
    conversions = {
        (0, 1): kilograms_to_pounds,
        (1, 0): pounds_to_kilograms,
        (2, 3): grams_to_ounces,
        (3, 2): ounces_to_grams
    }
    
    from_idx = unit_map.get(from_unit)
    to_idx = unit_map.get(to_unit)
    
    if from_idx is None or to_idx is None:
        raise ValueError(f"Unsupported units: {from_unit}, {to_unit}")
    
    if from_idx == to_idx:
        return value
    
    if (from_idx, to_idx) in conversions:
        return conversions[(from_idx, to_idx)](value)
    
    if from_idx in [0, 1]:
        if to_idx == 2:
            if from_idx == 0:
                return value * 1000
            else:
                return pounds_to_kilograms(value) * 1000
        elif to_idx == 3:
            if from_idx == 0:
                return grams_to_ounces(value * 1000)
            else:
                return grams_to_ounces(pounds_to_kilograms(value) * 1000)
    elif from_idx in [2, 3]:
        if to_idx == 0:
            if from_idx == 2:
                return value / 1000
            else:
                return ounces_to_grams(value) / 1000
        elif to_idx == 1:
            if from_idx == 2:
                return kilograms_to_pounds(value / 1000)
            else:
                return kilograms_to_pounds(ounces_to_grams(value) / 1000)
    
    raise ValueError(f"No conversion path from {from_unit} to {to_unit}")

def convert_volume(value, from_unit, to_unit):
    unit_map = {
        'L': 0,
        'gal': 1,
        'ml': 2,
        'floz': 3
    }
    
    conversions = {
        (0, 1): liters_to_gallons,
        (1, 0): gallons_to_liters,
        (2, 3): milliliters_to_fluid_ounces,
        (3, 2): fluid_ounces_to_milliliters
    }
    
    from_idx = unit_map.get(from_unit)
    to_idx = unit_map.get(to_unit)
    
    if from_idx is None or to_idx is None:
        raise ValueError(f"Unsupported units: {from_unit}, {to_unit}")
    
    if from_idx == to_idx:
        return value
    
    if (from_idx, to_idx) in conversions:
        return conversions[(from_idx, to_idx)](value)
    
    if from_idx in [0, 1]:
        if to_idx == 2:
            if from_idx == 0:
                return value * 1000
            else:
                return gallons_to_liters(value) * 1000
        elif to_idx == 3:
            if from_idx == 0:
                return milliliters_to_fluid_ounces(value * 1000)
            else:
                return milliliters_to_fluid_ounces(gallons_to_liters(value) * 1000)
    elif from_idx in [2, 3]:
        if to_idx == 0:
            if from_idx == 2:
                return value / 1000
            else:
                return fluid_ounces_to_milliliters(value) / 1000
        elif to_idx == 1:
            if from_idx == 2:
                return liters_to_gallons(value / 1000)
            else:
                return liters_to_gallons(fluid_ounces_to_milliliters(value) / 1000)
    
    raise ValueError(f"No conversion path from {from_unit} to {to_unit}")

def convert_temperature(value, from_unit, to_unit):
    if from_unit == to_unit:
        return value
    
    if from_unit == 'C' and to_unit == 'F':
        return celsius_to_fahrenheit(value)
    elif from_unit == 'F' and to_unit == 'C':
        return fahrenheit_to_celsius(value)
    else:
        raise ValueError(f"Unsupported temperature units: {from_unit}, {to_unit}")

if __name__ == '__main__':
    print(kilometers_to_miles(10))
    print(miles_to_kilometers(10))
    print(meters_to_feet(100))
    print(feet_to_meters(100))
    print(centimeters_to_inches(100))
    print(inches_to_centimeters(100))
    print(celsius_to_fahrenheit(100))
    print(fahrenheit_to_celsius(212))
    print(kilograms_to_pounds(10))
    print(pounds_to_kilograms(22.0462))
    print(grams_to_ounces(100))
    print(ounces_to_grams(3.5274))
    print(liters_to_gallons(10))
    print(gallons_to_liters(2.64172))
    print(milliliters_to_fluid_ounces(100))
    print(fluid_ounces_to_milliliters(3.3814))
    print(convert_distance(10, 'km', 'mi'))
    print(convert_distance(100, 'm', 'ft'))
    print(convert_weight(10, 'kg', 'lbs'))
    print(convert_weight(100, 'g', 'oz'))
    print(convert_volume(10, 'L', 'gal'))
    print(convert_volume(100, 'ml', 'floz'))
    print(convert_temperature(100, 'C', 'F'))
    print(convert_temperature(212, 'F', 'C'))