class LengthConversionError(Exception):
    def __init__(self, message, details):
        super().__init__(message)
        self.details = details

class UnsupportedUnitError(LengthConversionError):
    def __init__(self, unit):
        supported = ['meters', 'feet', 'inches', 'centimeters']
        message = f"Unit '{unit}' is not supported. Supported units: {', '.join(supported)}"
        details = {"unit": unit, "supported": supported}
        super().__init__(message, details)

class InvalidValueError(LengthConversionError):
    def __init__(self, value):
        message = f"Value must be a positive number, got: {value}"
        details = {"value": value}
        super().__init__(message, details)

class ZeroValueError(LengthConversionError):
    def __init__(self, value):
        message = f"Value cannot be zero: {value}"
        details = {"value": value}
        super().__init__(message, details)

METERS_TO_FEET = 3.28084
METERS_TO_INCHES = 39.3701
METERS_TO_CENTIMETERS = 100.0
FEET_TO_METERS = 1 / METERS_TO_FEET
INCHES_TO_METERS = 1 / METERS_TO_INCHES
CENTIMETERS_TO_METERS = 1 / METERS_TO_CENTIMETERS

def convert_length(value, from_unit, to_unit):
    supported_units = ['meters', 'feet', 'inches', 'centimeters']
    
    if not isinstance(value, (int, float)):
        raise InvalidValueError(value)
    
    if value < 0:
        raise InvalidValueError(value)
        
    if value == 0:
        raise ZeroValueError(value)
        
    if from_unit not in supported_units:
        raise UnsupportedUnitError(from_unit)
        
    if to_unit not in supported_units:
        raise UnsupportedUnitError(to_unit)
        
    if from_unit == to_unit:
        return value
        
    meters = 0.0
    
    if from_unit == 'meters':
        meters = value
    elif from_unit == 'feet':
        meters = value * FEET_TO_METERS
    elif from_unit == 'inches':
        meters = value * INCHES_TO_METERS
    elif from_unit == 'centimeters':
        meters = value * CENTIMETERS_TO_METERS
        
    if to_unit == 'meters':
        return meters
    elif to_unit == 'feet':
        return meters * METERS_TO_FEET
    elif to_unit == 'inches':
        return meters * METERS_TO_INCHES
    elif to_unit == 'centimeters':
        return meters * METERS_TO_CENTIMETERS

if __name__ == '__main__':
    result = convert_length(10, 'feet', 'meters')
    print(result)
    result2 = convert_length(100, 'centimeters', 'inches')
    print(result2)