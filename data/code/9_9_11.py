class ConversionError(Exception):
    def __init__(self, message, context):
        super().__init__(message)
        self.context = context

class UnitNotFoundError(ConversionError):
    def __init__(self, unit, available_units):
        message = f"Unit '{unit}' not found. Available units: {', '.join(available_units)}"
        super().__init__(message, {"requested_unit": unit, "available": available_units})

class NegativeValueError(ConversionError):
    def __init__(self, value):
        message = f"Value cannot be negative: {value}"
        super().__init__(message, {"value": value})

class ZeroValueError(ConversionError):
    def __init__(self, value):
        message = f"Value cannot be zero: {value}"
        super().__init__(message, {"value": value})

UNIT_FACTORS = {
    "meter": 1.0,
    "kilometer": 1000.0,
    "centimeter": 0.01,
    "millimeter": 0.001,
    "mile": 1609.344,
    "yard": 0.9144,
    "foot": 0.3048,
    "inch": 0.0254
}

def validate_value(value):
    if not isinstance(value, (int, float)):
        raise TypeError("Value must be a number")
    if value < 0:
        raise NegativeValueError(value)
    if value == 0:
        raise ZeroValueError(value)

def validate_unit(unit, available_units):
    if unit not in available_units:
        raise UnitNotFoundError(unit, available_units)

def convert_length(value, from_unit, to_unit):
    validate_value(value)
    validate_unit(from_unit, UNIT_FACTORS.keys())
    validate_unit(to_unit, UNIT_FACTORS.keys())
    
    base_value = value * UNIT_FACTORS[from_unit]
    result = base_value / UNIT_FACTORS[to_unit]
    return result

if __name__ == "__main__":
    test_cases = [
        (100, "centimeter", "meter"),
        (5, "mile", "kilometer"),
        (1, "foot", "inch"),
        (1000, "meter", "kilometer")
    ]
    
    results = []
    for val, f_unit, t_unit in test_cases:
        converted = convert_length(val, f_unit, t_unit)
        results.append(converted)
    
    print(results)