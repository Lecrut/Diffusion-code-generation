class TemperatureConversionError(Exception):
    def __init__(self, message, metadata):
        super().__init__(message)
        self.metadata = metadata

class UnsupportedUnitError(TemperatureConversionError):
    def __init__(self, unit, supported_units):
        message = f"Unit '{unit}' is not supported. Supported units: {supported_units}"
        metadata = {"unit": unit, "supported": list(supported_units)}
        super().__init__(message, metadata)

class InvalidTemperatureError(TemperatureConversionError):
    def __init__(self, value, absolute_zero):
        message = f"Temperature {value} is below absolute zero ({absolute_zero})"
        metadata = {"value": value, "absolute_zero": absolute_zero}
        super().__init__(message, metadata)

class NonNumericValueError(TemperatureConversionError):
    def __init__(self, value):
        message = f"Value must be numeric, got {type(value).__name__}: {value}"
        metadata = {"value": value, "type": type(value).__name__}
        super().__init__(message, metadata)

class TemperatureConverter:
    SUPPORTED_UNITS = ('celsius', 'fahrenheit', 'kelvin')
    ABSOLUTE_ZERO_C = -273.15
    
    def __init__(self, value, unit):
        self._validate_value(value)
        self._validate_unit(unit)
        self.celsius = self._to_celsius(float(value), unit)
    
    def _validate_value(self, value):
        if not isinstance(value, (int, float)):
            raise NonNumericValueError(value)
        celsius_equiv = self._to_celsius(float(value), 'celsius')
        if celsius_equiv < self.ABSOLUTE_ZERO_C:
            raise InvalidTemperatureError(float(value), self.ABSOLUTE_ZERO_C)
    
    def _validate_unit(self, unit):
        if unit not in self.SUPPORTED_UNITS:
            raise UnsupportedUnitError(unit, self.SUPPORTED_UNITS)
    
    def _to_celsius(self, value, unit):
        if unit == 'celsius':
            return value
        elif unit == 'fahrenheit':
            return (value - 32) * 5 / 9
        elif unit == 'kelvin':
            return value - 273.15
    
    def convert_to(self, target_unit):
        if target_unit not in self.SUPPORTED_UNITS:
            raise UnsupportedUnitError(target_unit, self.SUPPORTED_UNITS)
        
        if target_unit == 'celsius':
            return self.celsius
        elif target_unit == 'fahrenheit':
            return self.celsius * 9 / 5 + 32
        elif target_unit == 'kelvin':
            return self.celsius + 273.15

if __name__ == '__main__':
    converter = TemperatureConverter(100, 'celsius')
    fahrenheit_result = converter.convert_to('fahrenheit')
    kelvin_result = converter.convert_to('kelvin')
    print(f"Fahrenheit: {fahrenheit_result}")
    print(f"Kelvin: {kelvin_result}")
    
    try:
        invalid_converter = TemperatureConverter(-500, 'celsius')
        invalid_converter.convert_to('fahrenheit')
    except InvalidTemperatureError as e:
        print(f"Caught invalid temperature: {e.metadata['value']}")
    
    try:
        bad_unit_converter = TemperatureConverter(100, 'rankine')
    except UnsupportedUnitError as e:
        print(f"Caught unsupported unit: {e.metadata['unit']}")
        
    try:
        non_numeric_converter = TemperatureConverter("not_a_number", 'celsius')
    except NonNumericValueError as e:
        print(f"Caught non-numeric value: {e.metadata['type']}")