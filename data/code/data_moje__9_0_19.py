def liters_to_ml(value):
    return value * 1000

def ml_to_liters(value):
    return value / 1000

def liters_to_cubic_meters(value):
    return value / 1000

def cubic_meters_to_liters(value):
    return value * 1000

def liters_to_gallons(value):
    return value * 0.264172

def gallons_to_liters(value):
    return value / 0.264172

def liters_to_cubic_inches(value):
    return value * 61.0237

def cubic_inches_to_liters(value):
    return value / 61.0237

def convert_volume(value, from_unit, to_unit):
    units = ['l', 'ml', 'm3', 'gal', 'in3']
    from_unit = from_unit.lower()
    to_unit = to_unit.lower()
    
    if from_unit not in units or to_unit not in units:
        return "Invalid unit"
    
    if from_unit == to_unit:
        return value
    
    if from_unit == 'l':
        liters = value
    elif from_unit == 'ml':
        liters = value / 1000
    elif from_unit == 'm3':
        liters = value * 1000
    elif from_unit == 'gal':
        liters = value / 0.264172
    elif from_unit == 'in3':
        liters = value / 61.0237
    
    if to_unit == 'l':
        return liters
    elif to_unit == 'ml':
        return liters * 1000
    elif to_unit == 'm3':
        return liters / 1000
    elif to_unit == 'gal':
        return liters * 0.264172
    elif to_unit == 'in3':
        return liters * 61.0237

if __name__ == '__main__':
    test_cases = [
        (1000, 'ml', 'l'),
        (1, 'l', 'gal'),
        (2, 'gal', 'l'),
        (1, 'm3', 'l'),
        (5, 'l', 'in3'),
        (305.1185, 'in3', 'l'),
        (1, 'l', 'l')
    ]
    
    for value, from_u, to_u in test_cases:
        result = convert_volume(value, from_u, to_u)
        print(f"{value} {from_u} equals {result} {to_u}")