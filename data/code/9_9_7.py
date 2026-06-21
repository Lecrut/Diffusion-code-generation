class ConversionError(Exception):
    def __init__(self, message, details):
        super().__init__(message)
        self.details = details

class UnitNotFoundError(ConversionError):
    def __init__(self, unit, available):
        message = f"Unit '{unit}' is not supported. Supported: {', '.join(available)}"
        super().__init__(message, {"unit": unit, "supported": available})

class InvalidValueError(ConversionError):
    def __init__(self, value):
        message = f"Value must be a positive number, got: {value}"
        super().__init__(message, {"value": value})

class ZeroValueError(ConversionError):
    def __init__(self, value):
        message = f"Value cannot be zero: {value}"
        super().__init__(message, {"value": value})

FEET_TO_METERS = 0.3048
INCHES_TO_METERS = 0.0254
METERS_TO_FEET = 1.0 / FEET_TO_METERS
METERS_TO_INCHES = 1.0 / INCHES_TO_METERS

def convert(value, unit):
    if not isinstance(value, (int, float)):
        raise InvalidValueError(value)
    
    if value < 0:
        raise InvalidValueError(value)
    
    if value == 0:
        raise ZeroValueError(value)
    
    supported_units = ['feet', 'meters', 'inches']
    if unit not in supported_units:
        raise UnitNotFoundError(unit, supported_units)
    
    if unit == 'feet':
        return value * FEET_TO_METERS
    elif unit == 'inches':
        return value * INCHES_TO_METERS
    elif unit == 'meters':
        return value
    else:
        raise UnitNotFoundError(unit, supported_units)

if __name__ == '__main__':
    result = convert(10, 'feet')
    print(result)
    
    result2 = convert(5, 'meters')
    print(result2)
    
    result3 = convert(12, 'inches')
    print(result3)