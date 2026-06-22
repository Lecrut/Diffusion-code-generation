class ConversionError(Exception):
    def __init__(self, message, metadata):
        super().__init__(message)
        self.metadata = metadata

class UnknownUnitError(ConversionError):
    def __init__(self, unit_name):
        supported = ["km", "m", "ft", "in"]
        message = f"Unknown unit '{unit_name}'. Supported units: {supported}"
        super().__init__(message, {"unit": unit_name, "supported": supported})

class NegativeValueError(ConversionError):
    def __init__(self, value):
        message = f"Value cannot be negative: {value}"
        super().__init__(message, {"value": value})

class ZeroValueError(ConversionError):
    def __init__(self, value):
        message = f"Value cannot be zero: {value}"
        super().__init__(message, {"value": value})

UNIT_FACTORS_TO_METERS = {
    "km": 1000.0,
    "m": 1.0,
    "ft": 0.3048,
    "in": 0.0254
}

def convert_unit(value, from_unit, to_unit):
    if from_unit not in UNIT_FACTORS_TO_METERS:
        raise UnknownUnitError(from_unit)
    if to_unit not in UNIT_FACTORS_TO_METERS:
        raise UnknownUnitError(to_unit)
    
    if value < 0:
        raise NegativeValueError(value)
    
    if value == 0:
        raise ZeroValueError(value)
    
    meters = value * UNIT_FACTORS_TO_METERS[from_unit]
    result = meters / UNIT_FACTORS_TO_METERS[to_unit]
    return result

if __name__ == '__main__':
    try:
        result1 = convert_unit(1000, "m", "km")
        print(result1)
        
        result2 = convert_unit(5, "km", "m")
        print(result2)
        
        result3 = convert_unit(6, "ft", "m")
        print(result3)
        
        result4 = convert_unit(12, "in", "ft")
        print(result4)
        
        try:
            convert_unit(10, "m", "invalid")
        except UnknownUnitError as e:
            print(str(e))
            
        try:
            convert_unit(-5, "m", "km")
        except NegativeValueError as e:
            print(str(e))
            
        try:
            convert_unit(0, "m", "km")
        except ZeroValueError as e:
            print(str(e))
            
    except Exception as e:
        print(str(e))