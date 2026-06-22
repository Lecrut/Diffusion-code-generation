class TemperatureConversionError(Exception):
    def __init__(self, message, context):
        super().__init__(message)
        self.context = context

class InvalidUnitError(TemperatureConversionError):
    def __init__(self, unit, valid_units):
        message = f"Unit '{unit}' is not valid. Valid units are: {valid_units}"
        super().__init__(message, {"invalid_unit": unit, "valid_units": valid_units})

class OutOfRangeError(TemperatureConversionError):
    def __init__(self, value, unit, minimum):
        message = f"Value {value} in {unit} is below absolute zero ({minimum})."
        super().__init__(message, {"value": value, "unit": unit, "minimum": minimum})

class ConversionLogicError(TemperatureConversionError):
    def __init__(self, details):
        message = "Conversion logic failed due to unsupported unit combination or internal error."
        super().__init__(message, details)

VALID_UNITS = ["C", "F", "K"]

def to_celsius(value, from_unit):
    if from_unit == "C":
        return value
    if from_unit == "F":
        return (value - 32) * 5 / 9
    if from_unit == "K":
        return value - 273.15
    raise ConversionLogicError({"reason": "Unexpected unit reached in to_celsius", "unit": from_unit})

def from_celsius(value, to_unit):
    if to_unit == "C":
        return value
    if to_unit == "F":
        return value * 9 / 5 + 32
    if to_unit == "K":
        return value + 273.15
    raise ConversionLogicError({"reason": "Unexpected unit reached in from_celsius", "unit": to_unit})

def validate_physical_constraints(value, unit):
    if unit == "K" and value < 0:
        raise OutOfRangeError(value, "K", 0)
    if unit == "C" and value < -273.15:
        raise OutOfRangeError(value, "C", -273.15)
    if unit == "F" and value < -459.67:
        raise OutOfRangeError(value, "F", -459.67)

def convert_temperature(value, from_unit, to_unit):
    if from_unit not in VALID_UNITS:
        raise InvalidUnitError(from_unit, VALID_UNITS)
    if to_unit not in VALID_UNITS:
        raise InvalidUnitError(to_unit, VALID_UNITS)
    
    validate_physical_constraints(value, from_unit)
    
    celsius_value = to_celsius(value, from_unit)
    result = from_celsius(celsius_value, to_unit)
    
    validate_physical_constraints(result, to_unit)
    
    return round(result, 2)

if __name__ == '__main__':
    print(convert_temperature(100, "C", "F"))
    print(convert_temperature(32, "F", "C"))
    print(convert_temperature(0, "C", "K"))
    
    try:
        convert_temperature(100, "X", "C")
    except InvalidUnitError as e:
        print(e)
        
    try:
        convert_temperature(-500, "K", "C")
    except OutOfRangeError as e:
        print(e)
        
    try:
        convert_temperature(300, "C", "Y")
    except InvalidUnitError as e:
        print(e)