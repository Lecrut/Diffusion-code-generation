class ConversionError(Exception):
    def __init__(self, message, context):
        super().__init__(message)
        self.context = context

class UnitNotFoundError(ConversionError):
    def __init__(self, unit, available_units):
        message = f"Unit '{unit}' is not supported. Supported: {', '.join(available_units)}"
        super().__init__(message, {"unit": unit, "available_units": available_units})

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
YARDS_TO_METERS = 0.9144

SUPPORTED_UNITS = ["feet", "inches", "yards", "meters"]
UNIT_TO_FACTOR = {
    "feet": FEET_TO_METERS,
    "inches": INCHES_TO_METERS,
    "yards": YARDS_TO_METERS,
    "meters": 1.0
}

def convert(value, unit):
    if unit not in SUPPORTED_UNITS:
        raise UnitNotFoundError(unit, SUPPORTED_UNITS)
    
    if not isinstance(value, (int, float)):
        raise InvalidValueError(value)
    
    if value < 0:
        raise InvalidValueError(value)
    
    if value == 0:
        raise ZeroValueError(value)
    
    factor = UNIT_TO_FACTOR[unit]
    result_in_meters = value * factor
    
    converted_feet = result_in_meters / FEET_TO_METERS
    converted_inches = result_in_meters / INCHES_TO_METERS
    converted_yards = result_in_meters / YARDS_TO_METERS
    converted_meters = result_in_meters / 1.0
    
    conversion_results = {
        "feet": converted_feet,
        "inches": converted_inches,
        "yards": converted_yards,
        "meters": converted_meters
    }
    
    return conversion_results

if __name__ == '__main__':
    sample_value = 10
    sample_unit = "feet"
    result = convert(sample_value, sample_unit)
    print(result)
    print(result["meters"])
    print(result["inches"])
    print(result["yards"])
    print(result["feet"])