class ConversionBaseError(Exception):
    def __init__(self, message, context):
        self.context = context
        super().__init__(message)

class UnitNotSupportedError(ConversionBaseError):
    def __init__(self, unit, available_units):
        message = f"Unit '{unit}' is not supported. Supported: {', '.join(available_units)}"
        super().__init__(message, {"unit": unit, "available": available_units})

class InvalidValueError(ConversionBaseError):
    def __init__(self, value):
        message = f"Value must be a positive number, got: {value}"
        super().__init__(message, {"value": value})

class ZeroValueError(ConversionBaseError):
    def __init__(self, value):
        message = f"Value cannot be zero: {value}"
        super().__init__(message, {"value": value})

FEET_TO_METERS = 0.3048
INCHES_TO_METERS = 0.0254
METERS_TO_FEET = 1 / FEET_TO_METERS
METERS_TO_INCHES = 1 / INCHES_TO_METERS

VALID_UNITS = ['feet', 'meters', 'inches']

def convert_length(value, from_unit, to_unit):
    if from_unit not in VALID_UNITS:
        raise UnitNotSupportedError(from_unit, VALID_UNITS)
    if to_unit not in VALID_UNITS:
        raise UnitNotSupportedError(to_unit, VALID_UNITS)
    if not isinstance(value, (int, float)):
        raise InvalidValueError(value)
    if value < 0:
        raise InvalidValueError(value)
    if value == 0:
        raise ZeroValueError(value)

    if from_unit == to_unit:
        return value

    if from_unit == 'meters':
        meters = value
    elif from_unit == 'feet':
        meters = value * FEET_TO_METERS
    elif from_unit == 'inches':
        meters = value * INCHES_TO_METERS
    else:
        meters = value

    if to_unit == 'meters':
        return meters
    elif to_unit == 'feet':
        return meters * METERS_TO_FEET
    elif to_unit == 'inches':
        return meters * METERS_TO_INCHES
    else:
        return meters

if __name__ == '__main__':
    print(convert_length(10, 'feet', 'meters'))
    print(convert_length(5.0, 'meters', 'feet'))
    print(convert_length(100, 'inches', 'feet'))
    print(convert_length(1, 'feet', 'feet'))