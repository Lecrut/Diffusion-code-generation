class ConversionBaseError(Exception):
    def __init__(self, message, context):
        super().__init__(message)
        self.context = context

class UnitNotSupportedError(ConversionBaseError):
    def __init__(self, target_unit, supported_units):
        message = f"Target unit '{target_unit}' is not supported. Supported units: {supported_units}"
        super().__init__(message, {"target_unit": target_unit, "supported_units": supported_units})

class InvalidValueError(ConversionBaseError):
    def __init__(self, value):
        message = f"Conversion value must be a positive number, received: {value}"
        super().__init__(message, {"value": value, "type": type(value).__name__})

class ZeroValueError(ConversionBaseError):
    def __init__(self, value):
        message = f"Conversion value cannot be zero, received: {value}"
        super().__init__(message, {"value": value})

class TemperatureUnitError(ConversionBaseError):
    def __init__(self, unit):
        message = f"Invalid temperature unit format: '{unit}'. Expected 'C', 'F', or 'K'."
        super().__init__(message, {"unit": unit})

CONVERSION_FACTORS = {
    "C": {"F": 9 / 5 + 32, "K": 273.15, "C": 1.0},
    "F": {"C": 5 / 9, "K": 5 / 9 * (9 / 5) + 32, "F": 1.0},
    "K": {"C": 1.0, "F": 9 / 5 * (1.0), "K": 1.0}
}

UNIT_MAP = {
    "C": {"C": 1.0, "F": 1.8, "K": 1.0},
    "F": {"C": 5 / 9, "F": 1.0, "K": 5 / 9},
    "K": {"C": 1.0, "F": 9 / 5, "K": 1.0}
}

def get_scale_factor(from_unit, to_unit):
    if from_unit == to_unit:
        return 1.0
    if from_unit == "C" and to_unit == "F":
        return 1.8
    if from_unit == "F" and to_unit == "C":
        return 5 / 9
    if from_unit == "C" and to_unit == "K":
        return 1.0
    if from_unit == "K" and to_unit == "C":
        return 1.0
    if from_unit == "F" and to_unit == "K":
        return 5 / 9
    if from_unit == "K" and to_unit == "F":
        return 9 / 5
    raise UnitNotSupportedError(to_unit, ["C", "F", "K"])

def validate_unit(unit, valid_units):
    if unit not in valid_units:
        raise UnitNotSupportedError(unit, list(valid_units))

def validate_value(value):
    if not isinstance(value, (int, float)):
        raise InvalidValueError(value)
    if value <= 0:
        if value == 0:
            raise ZeroValueError(value)
        raise InvalidValueError(value)

def convert_temperature(value, from_unit, to_unit):
    valid_units = {"C", "F", "K"}
    validate_unit(from_unit, valid_units)
    validate_unit(to_unit, valid_units)
    validate_value(value)
    if from_unit == "C" and to_unit == "F":
        return value * 1.8 + 32
    if from_unit == "F" and to_unit == "C":
        return (value - 32) * 5 / 9
    if from_unit == "C" and to_unit == "K":
        return value + 273.15
    if from_unit == "K" and to_unit == "C":
        return value - 273.15
    if from_unit == "F" and to_unit == "K":
        return (value - 32) * 5 / 9 + 273.15
    if from_unit == "K" and to_unit == "F":
        return (value - 273.15) * 9 / 5 + 32
    return value

class TemperatureConverter:
    def __init__(self):
        self.history = []

    def convert(self, value, from_unit, to_unit):
        result = convert_temperature(value, from_unit, to_unit)
        self.history.append({"input": value, "from": from_unit, "to": to_unit, "output": result})
        return result

    def get_last_result(self):
        if not self.history:
            return None
        return self.history[-1]["output"]

if __name__ == '__main__':
    converter = TemperatureConverter()
    test_cases = [
        (100, "C", "F"),
        (212, "F", "C"),
        (273.15, "K", "C"),
        (0, "C", "K")
    ]
    for val, src, dest in test_cases:
        try:
            res = converter.convert(val, src, dest)
            print(f"Converted {val} {src} to {res} {dest}")
        except ConversionBaseError as e:
            print(f"Error: {e}")
    print(f"Last computed value: {converter.get_last_result()}")