class InvalidConversionUnitError(Exception):
    def __init__(self, unit):
        message = f"Unsupported conversion unit: {unit}"
        super().__init__(message)
        self.unit = unit

class NegativeValueError(Exception):
    def __init__(self, value):
        message = f"Value cannot be negative: {value}"
        super().__init__(message)
        self.value = value

class ConversionFactorError(Exception):
    def __init__(self, from_unit, to_unit):
        message = f"No conversion factor defined from {from_unit} to {to_unit}"
        super().__init__(message)
        self.from_unit = from_unit
        self.to_unit = to_unit

CONVERSION_FACTORS = {
    ("km", "m"): 1000,
    ("m", "km"): 0.001,
    ("ft", "m"): 0.3048,
    ("m", "ft"): 3.28084,
    ("lb", "kg"): 0.453592,
    ("kg", "lb"): 2.20462,
    ("celsius", "fahrenheit"): lambda x: (x * 9/5) + 32,
    ("fahrenheit", "celsius"): lambda x: (x - 32) * 5/9,
}

def convert(value, from_unit, to_unit):
    if value < 0 and from_unit not in ("celsius", "fahrenheit"):
        raise NegativeValueError(value)
    
    if from_unit == to_unit:
        return value
    
    key = (from_unit, to_unit)
    
    if key not in CONVERSION_FACTORS:
        raise ConversionFactorError(from_unit, to_unit)
    
    factor_or_func = CONVERSION_FACTORS[key]
    
    if callable(factor_or_func):
        result = factor_or_func(value)
    else:
        result = value * factor_or_func
    
    return result

if __name__ == '__main__':
    sample_results = []
    
    try:
        result1 = convert(5, "km", "m")
        sample_results.append(("km_to_m", result1))
    except Exception as e:
        sample_results.append(("km_to_m", str(e)))
    
    try:
        result2 = convert(100, "m", "km")
        sample_results.append(("m_to_km", result2))
    except Exception as e:
        sample_results.append(("m_to_km", str(e)))
    
    try:
        result3 = convert(-10, "km", "m")
        sample_results.append(("negative_km", result3))
    except NegativeValueError as e:
        sample_results.append(("negative_km", f"NegativeValueError: {e.value}"))
    except Exception as e:
        sample_results.append(("negative_km", str(e)))
    
    try:
        result4 = convert(20, "celsius", "fahrenheit")
        sample_results.append(("celsius_to_fahrenheit", result4))
    except Exception as e:
        sample_results.append(("celsius_to_fahrenheit", str(e)))
    
    try:
        result5 = convert(100, "invalid_unit", "m")
        sample_results.append(("invalid_unit", result5))
    except ConversionFactorError as e:
        sample_results.append(("invalid_unit", f"ConversionFactorError: {e.from_unit} -> {e.to_unit}"))
    except Exception as e:
        sample_results.append(("invalid_unit", str(e)))
    
    for test_name, result in sample_results:
        print(f"{test_name}: {result}")