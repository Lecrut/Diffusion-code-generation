class LengthConversionError(Exception):
    def __init__(self, message, context):
        self.context = context
        super().__init__(message)

class UnsupportedUnitError(LengthConversionError):
    def __init__(self, unit):
        supported_units = ['feet', 'meters', 'inches']
        message = f"Unit '{unit}' is not supported. Supported units are: {', '.join(supported_units)}"
        context = {"unit": unit, "supported": supported_units}
        super().__init__(message, context)

class NegativeValueError(LengthConversionError):
    def __init__(self, value):
        message = f"Value must be non-negative, got: {value}"
        context = {"value": value}
        super().__init__(message, context)

class ZeroValueError(LengthConversionError):
    def __init__(self, value):
        message = f"Value cannot be zero, got: {value}"
        context = {"value": value}
        super().__init__(message, context)

FEET_TO_METERS = 0.3048
METERS_TO_FEET = 1.0 / FEET_TO_METERS
INCHES_TO_METERS = 0.0254
METERS_TO_INCHES = 1.0 / INCHES_TO_METERS

def convert_length(value, unit, target_unit):
    if value < 0:
        raise NegativeValueError(value)
    if value == 0:
        raise ZeroValueError(value)
    
    supported_units = ['feet', 'meters', 'inches']
    if unit not in supported_units:
        raise UnsupportedUnitError(unit)
    if target_unit not in supported_units:
        raise UnsupportedUnitError(target_unit)
    
    if unit == target_unit:
        return value
    
    value_in_meters = 0.0
    if unit == 'feet':
        value_in_meters = value * FEET_TO_METERS
    elif unit == 'meters':
        value_in_meters = value
    elif unit == 'inches':
        value_in_meters = value * INCHES_TO_METERS
    
    if target_unit == 'feet':
        return value_in_meters / FEET_TO_METERS
    elif target_unit == 'meters':
        return value_in_meters
    elif target_unit == 'inches':
        return value_in_meters / INCHES_TO_METERS

if __name__ == '__main__':
    result = convert_length(10.0, 'feet', 'meters')
    print(result)
    
    result2 = convert_length(1.0, 'meters', 'feet')
    print(result2)
    
    result3 = convert_length(12.0, 'inches', 'feet')
    print(result3)