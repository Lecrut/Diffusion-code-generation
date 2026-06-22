class ConversionError(Exception):
    def __init__(self, message, metadata):
        super().__init__(message)
        self.metadata = metadata

class UnsupportedUnitError(ConversionError):
    def __init__(self, unit, supported_units):
        message = f"Unit {unit} is not supported. Valid units are {supported_units}"
        super().__init__(message, {"unit": unit, "supported": supported_units})

class InvalidValueError(ConversionError):
    def __init__(self, value):
        message = f"Value must be a positive number, got {value}"
        super().__init__(message, {"value": value})

class ZeroDivisionError(ConversionError):
    def __init__(self):
        message = "Cannot divide by zero"
        super().__init__(message, {})

UNIT_CONVERSIONS = {
    "celsius": {"fahrenheit": lambda x: x * 9/5 + 32, "kelvin": lambda x: x + 273.15},
    "fahrenheit": {"celsius": lambda x: (x - 32) * 5/9, "kelvin": lambda x: (x - 32) * 5/9 + 273.15},
    "kelvin": {"celsius": lambda x: x - 273.15, "fahrenheit": lambda x: (x - 273.15) * 9/5 + 32}
}

def convert_temperature(value, from_unit, to_unit):
    if not isinstance(value, (int, float)):
        raise InvalidValueError(value)
    if value < 0 and from_unit.lower() == "kelvin":
        raise InvalidValueError(value)
    from_lower = from_unit.lower()
    to_lower = to_unit.lower()
    if from_lower not in UNIT_CONVERSIONS:
        raise UnsupportedUnitError(from_unit, list(UNIT_CONVERSIONS.keys()))
    if to_lower not in UNIT_CONVERSIONS[from_lower]:
        raise UnsupportedUnitError(to_unit, list(UNIT_CONVERSIONS[from_lower].keys()))
    if from_lower == to_lower:
        return value
    conversion_function = UNIT_CONVERSIONS[from_lower][to_lower]
    return conversion_function(value)

if __name__ == '__main__':
    result1 = convert_temperature(100, "celsius", "fahrenheit")
    print(result1)
    result2 = convert_temperature(32, "fahrenheit", "celsius")
    print(result2)
    result3 = convert_temperature(0, "celsius", "kelvin")
    print(result3)
    try:
        convert_temperature(-10, "kelvin", "celsius")
    except ConversionError as e:
        print(str(e))
    try:
        convert_temperature(100, "celsius", "rankine")
    except ConversionError as e:
        print(str(e))
    try:
        convert_temperature("hot", "celsius", "fahrenheit")
    except ConversionError as e:
        print(str(e))