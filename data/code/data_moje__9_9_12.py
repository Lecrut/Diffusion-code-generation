class ConversionBaseError(Exception):
    def __init__(self, message, context):
        super().__init__(message)
        self.context = context

class UnsupportedUnitError(ConversionBaseError):
    def __init__(self, unit, supported_units):
        message = f"Unit '{unit}' is not supported. Supported: {', '.join(supported_units)}"
        super().__init__(message, {"unit": unit, "supported_units": supported_units})

class InvalidInputError(ConversionBaseError):
    def __init__(self, value):
        message = f"Value must be a positive number, got: {value}"
        super().__init__(message, {"value": value})

class ZeroInputError(ConversionBaseError):
    def __init__(self, value):
        message = f"Value cannot be zero: {value}"
        super().__init__(message, {"value": value})

KILOMETERS_TO_MILES = 0.621371
MILES_TO_KILOMETERS = 1.60934

def convert_distance(value, unit_from, unit_to):
    if value < 0:
        raise InvalidInputError(value)
    if value == 0:
        raise ZeroInputError(value)

    unit_from_lower = unit_from.lower()
    unit_to_lower = unit_to.lower()

    supported_units = ['kilometers', 'miles']

    if unit_from_lower not in supported_units:
        raise UnsupportedUnitError(unit_from_lower, supported_units)
    if unit_to_lower not in supported_units:
        raise UnsupportedUnitError(unit_to_lower, supported_units)

    if unit_from_lower == unit_to_lower:
        return value

    if unit_from_lower == 'kilometers' and unit_to_lower == 'miles':
        return value * KILOMETERS_TO_MILES
    elif unit_from_lower == 'miles' and unit_to_lower == 'kilometers':
        return value * MILES_TO_KILOMETERS
    else:
        raise UnsupportedUnitError(unit_to_lower, supported_units)

if __name__ == '__main__':
    result = convert_distance(10, 'km', 'miles')
    print(result)

    result2 = convert_distance(5.0, 'miles', 'kilometers')
    print(result2)

    try:
        convert_distance(-10, 'kilometers', 'miles')
    except ZeroInputError as e:
        print(f"Error: {e.args[0]}")

    try:
        convert_distance(0, 'kilometers', 'miles')
    except ZeroInputError as e:
        print(f"Error: {e.args[0]}")