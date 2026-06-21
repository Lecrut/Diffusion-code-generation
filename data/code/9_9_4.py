class ConversionException(Exception):
    def __init__(self, message, context_data):
        super().__init__(message)
        self.context_data = context_data

class UnsupportedUnitError(ConversionException):
    def __init__(self, unit, supported_units):
        message = f"Unit '{unit}' is not supported. Supported units are: {supported_units}"
        super().__init__(message, {"unit": unit, "supported": supported_units})

class NonPositiveValueError(ConversionException):
    def __init__(self, value):
        message = f"Value must be positive, got: {value}"
        super().__init__(message, {"value": value})

def get_conversion_factor(unit):
    rates = {
        "km": 1000.0,
        "m": 1.0,
        "cm": 0.01,
        "mm": 0.001,
        "in": 0.0254,
        "ft": 0.3048,
        "yd": 0.9144,
        "mi": 1609.34
    }
    if unit not in rates:
        raise UnsupportedUnitError(unit, list(rates.keys()))
    return rates[unit]

def convert_length(value, source_unit, target_unit):
    if not isinstance(value, (int, float)):
        raise NonPositiveValueError(value)
    if value <= 0:
        raise NonPositiveValueError(value)
    
    source_factor = get_conversion_factor(source_unit)
    target_factor = get_conversion_factor(target_unit)
    
    meters = value * source_factor
    result = meters / target_factor
    
    return result

def run_conversion_demo():
    try:
        result1 = convert_length(5.0, "ft", "m")
        result2 = convert_length(100, "cm", "in")
        result3 = convert_length(1, "mi", "km")
        return {
            "feet_to_meters": result1,
            "cm_to_inches": result2,
            "miles_to_km": result3
        }
    except ConversionException as e:
        return {
            "error": str(e),
            "context": e.context_data
        }

if __name__ == '__main__':
    output = run_conversion_demo()
    print(output)