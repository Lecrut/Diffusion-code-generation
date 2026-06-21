class ConversionBaseError(Exception):
    def __init__(self, message, data):
        super().__init__(message)
        self.data = data

class UnitNotSupportedError(ConversionBaseError):
    def __init__(self, unit):
        supported = ['feet', 'meters']
        message = f"Unit '{unit}' is not supported. Supported: {supported}"
        super().__init__(message, {"unit": unit, "supported": supported})

class InvalidValueError(ConversionBaseError):
    def __init__(self, value):
        message = f"Value must be a positive number, got: {value}"
        super().__init__(message, {"value": value})

class ZeroValueError(ConversionBaseError):
    def __init__(self, value):
        message = f"Value cannot be zero: {value}"
        super().__init__(message, {"value": value})

def convert(value, unit):
    if not isinstance(value, (int, float)):
        raise InvalidValueError(value)
    if value <= 0:
        raise ZeroValueError(value)
    
    feet_to_meters_factor = 0.3048
    
    if unit == 'feet':
        return value * feet_to_meters_factor
    elif unit == 'meters':
        return value / feet_to_meters_factor
    else:
        raise UnitNotSupportedError(unit)

def format_result(value, unit, converted_value):
    return f"{value} {unit} = {converted_value:.4f} meters"

if __name__ == '__main__':
    try:
        result = convert(10, 'feet')
        output = format_result(10, 'feet', result)
        print(output)
    except ConversionBaseError as e:
        print(f"Error: {e}")