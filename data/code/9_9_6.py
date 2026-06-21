class ConversionException(Exception):
    def __init__(self, message, code):
        super().__init__(message)
        self.error_code = code

class NegativeValueError(ConversionException):
    def __init__(self, value):
        super().__init__(f"Cannot convert negative value: {value}", "NEGATIVE_VALUE")

class InvalidUnitError(ConversionException):
    def __init__(self, unit, supported_units):
        super().__init__(f"Unsupported unit: {unit}. Supported: {supported_units}", "INVALID_UNIT")

class ConversionEngine:
    def __init__(self, rates):
        self.rates = rates
        self.base_unit = "meter"

    def _validate_unit(self, unit):
        if unit not in self.rates:
            raise InvalidUnitError(unit, list(self.rates.keys()))

    def _normalize_to_base(self, value, unit):
        self._validate_unit(unit)
        if value < 0:
            raise NegativeValueError(value)
        return value * self.rates[unit]

    def _convert_from_base(self, base_value, target_unit):
        self._validate_unit(target_unit)
        return base_value / self.rates[target_unit]

    def convert(self, value, source, target):
        base_value = self._normalize_to_base(value, source)
        return self._convert_from_base(base_value, target)

def run_sample():
    metric_rates = {
        "meter": 1.0,
        "kilometer": 1000.0,
        "centimeter": 0.01,
        "millimeter": 0.001,
        "mile": 1609.344,
        "yard": 0.9144,
        "foot": 0.3048,
        "inch": 0.0254
    }

    engine = ConversionEngine(metric_rates)

    try:
        result_1 = engine.convert(5.0, "foot", "meter")
        print(result_1)
    except ConversionException as e:
        print(f"Error: {e}")

    try:
        result_2 = engine.convert(1.0, "mile", "kilometer")
        print(result_2)
    except ConversionException as e:
        print(f"Error: {e}")

    try:
        engine.convert(-10.0, "meter", "foot")
    except NegativeValueError as e:
        print(e.args[0])

    try:
        engine.convert(100, "league", "meter")
    except InvalidUnitError as e:
        print(e.args[0])

if __name__ == '__main__':
    run_sample()