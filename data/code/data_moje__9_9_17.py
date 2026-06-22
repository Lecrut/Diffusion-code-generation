class ConversionBaseError(Exception):
    def __init__(self, message, context):
        super().__init__(message)
        self.context = context

class UnsupportedUnitError(ConversionBaseError):
    def __init__(self, unit, supported_units):
        message = f"Unit '{unit}' is not supported. Supported units: {', '.join(supported_units)}"
        super().__init__(message, {"unit": unit, "supported_units": supported_units})

class InvalidValueError(ConversionBaseError):
    def __init__(self, value):
        message = f"Value must be a positive number, got: {value}"
        super().__init__(message, {"value": value})

class NegativeValueError(ConversionBaseError):
    def __init__(self, value):
        message = f"Value cannot be negative: {value}"
        super().__init__(message, {"value": value})

SUPPORTED_UNITS = {'celsius', 'fahrenheit', 'kelvin'}

def _convert_to_kelvin(value, from_unit):
    if from_unit == 'kelvin':
        return value
    if from_unit == 'celsius':
        return value + 273.15
    if from_unit == 'fahrenheit':
        return (value - 32) * 5 / 9 + 273.15
    return value

def _convert_from_kelvin(value, to_unit):
    if to_unit == 'kelvin':
        return value
    if to_unit == 'celsius':
        return value - 273.15
    if to_unit == 'fahrenheit':
        return (value - 273.15) * 9 / 5 + 32
    return value

def convert_temperature(value, from_unit, to_unit):
    from_unit = from_unit.lower()
    to_unit = to_unit.lower()

    if from_unit not in SUPPORTED_UNITS:
        raise UnsupportedUnitError(from_unit, SUPPORTED_UNITS)
    if to_unit not in SUPPORTED_UNITS:
        raise UnsupportedUnitError(to_unit, SUPPORTED_UNITS)

    if not isinstance(value, (int, float)):
        raise InvalidValueError(value)

    if value < 0 and from_unit != 'celsius' and from_unit != 'fahrenheit':
        raise NegativeValueError(value)

    if from_unit == to_unit:
        return value

    kelvin_value = _convert_to_kelvin(value, from_unit)
    result = _convert_from_kelvin(kelvin_value, to_unit)
    return result

if __name__ == '__main__':
    try:
        result1 = convert_temperature(100, 'celsius', 'fahrenheit')
        print(result1)
        result2 = convert_temperature(32, 'fahrenheit', 'celsius')
        print(result2)
        result3 = convert_temperature(300, 'kelvin', 'celsius')
        print(result3)
        print(convert_temperature(0, 'celsius', 'kelvin'))
    except ConversionBaseError as e:
        print(f"Error: {e}")