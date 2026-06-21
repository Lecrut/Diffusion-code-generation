class UnitConversionError(Exception):
    def __init__(self, message, context=None):
        self.context = context or {}
        super().__init__(message)

class UnsupportedUnitError(UnitConversionError):
    def __init__(self, unit, supported):
        self.supported_units = supported
        message = f"Unit '{unit}' is not supported. Supported: {', '.join(supported)}"
        super().__init__(message, {"unit": unit, "supported": supported})

class InvalidValueError(UnitConversionError):
    def __init__(self, value):
        message = f"Value must be a non-negative number, got: {value}"
        super().__init__(message, {"value": value})

class ZeroValueError(UnitConversionError):
    def __init__(self, value):
        message = f"Value cannot be zero: {value}"
        super().__init__(message, {"value": value})

METERS_PER_INCH = 0.0254
METERS_PER_FOOT = 0.3048
METERS_PER_YARD = 0.9144
METERS_PER_MILE = 1609.344
METERS_PER_CM = 0.01
METERS_PER_MM = 0.001
METERS_PER_KM = 1000.0

SUPPORTED_LENGTH_UNITS = {
    'm': METERS_PER_MILE, 
    'ft': METERS_PER_FOOT, 
    'in': METERS_PER_INCH, 
    'km': METERS_PER_KM, 
    'cm': METERS_PER_CM, 
    'mm': METERS_PER_MM, 
    'mi': METERS_PER_MILE, 
    'yd': METERS_PER_YARD
}

SUPPORTED_LENGTH_UNITS['m'] = 1.0

def convert_length(value, from_unit, to_unit):
    if from_unit not in SUPPORTED_LENGTH_UNITS:
        raise UnsupportedUnitError(from_unit, list(SUPPORTED_LENGTH_UNITS.keys()))
    if to_unit not in SUPPORTED_LENGTH_UNITS:
        raise UnsupportedUnitError(to_unit, list(SUPPORTED_LENGTH_UNITS.keys()))
    if value < 0:
        raise InvalidValueError(value)
    if value == 0:
        raise ZeroValueError(value)
    
    meters = value * SUPPORTED_LENGTH_UNITS[from_unit]
    
    if to_unit == 'm':
        return meters
    
    return meters / SUPPORTED_LENGTH_UNITS[to_unit]

def convert_temperature(value, from_unit, to_unit):
    if from_unit not in ('C', 'F', 'K'):
        raise UnsupportedUnitError(from_unit, ['C', 'F', 'K'])
    if to_unit not in ('C', 'F', 'K'):
        raise UnsupportedUnitError(to_unit, ['C', 'F', 'K'])
    
    if value < -273.15:
        raise InvalidValueError(value)
    
    if from_unit == to_unit:
        return value
    
    celsius = value
    
    if from_unit == 'F':
        celsius = (value - 32) * 5 / 9
    elif from_unit == 'K':
        celsius = value - 273.15
    
    if to_unit == 'C':
        return celsius
    elif to_unit == 'F':
        return (celsius * 9 / 5) + 32
    elif to_unit == 'K':
        return celsius + 273.15

def convert_weight(value, from_unit, to_unit):
    if from_unit not in ('kg', 'g', 'lb', 'oz'):
        raise UnsupportedUnitError(from_unit, ['kg', 'g', 'lb', 'oz'])
    if to_unit not in ('kg', 'g', 'lb', 'oz'):
        raise UnsupportedUnitError(to_unit, ['kg', 'g', 'lb', 'oz'])
    
    if value < 0:
        raise InvalidValueError(value)
    
    grams = value
    
    if from_unit == 'kg':
        grams = value * 1000
    elif from_unit == 'lb':
        grams = value * 453.59237
    elif from_unit == 'oz':
        grams = value * 28.349523125
    
    if to_unit == 'g':
        return grams
    elif to_unit == 'kg':
        return grams / 1000
    elif to_unit == 'lb':
        return grams / 453.59237
    elif to_unit == 'oz':
        return grams / 28.349523125

if __name__ == '__main__':
    result = convert_length(10, 'ft', 'm')
    print(f"10 ft in meters: {result}")
    
    result = convert_temperature(212, 'F', 'C')
    print(f"212 F in Celsius: {result}")
    
    result = convert_weight(1, 'lb', 'kg')
    print(f"1 lb in kg: {result}")
    
    try:
        convert_length(-1, 'ft', 'm')
    except InvalidValueError as e:
        print(f"Caught error: {e}")