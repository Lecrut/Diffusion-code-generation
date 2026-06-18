class ConversionError(Exception):
    """Base exception for conversion errors."""
    pass

class InvalidDataTypeError(ConversionError):
    """Raised when the input data is not in an expected format or type."""
    def __init__(self, message: str, original_value=None):
        self.original_value = original_value
        super().__init__(message)

    def __str__(self):
        if self.original_value is not None:
            return f"{super().__str__()} - Original value: {self.original_value}"
        return super().__str__()

class ZeroDivisionError(ConversionError):
    """Raised when division by zero occurs during conversion."""
    pass

class ConversionScript:
    def __init__(self, from_unit: str, to_unit: str):
        self.from_unit = from_unit.lower()
        self.to_unit = to_unit.lower()

    def _validate_units(self) -> None:
        """Validates that both units are supported."""
        supported_units = ['celsius', 'fahrenheit', 'kelvin']
        
        if self.from_unit not in supported_units or self.to_unit not in supported_units:
            raise InvalidDataTypeError(
                "Unsupported unit. Supported units: celsius, fahrenheit, kelvin.",
                original_value=self.from_unit + "/" + self.to_unit
            )

    def convert_temperature(self, value) -> float:
        """Converts temperature from one unit to another."""
        self._validate_units()

        # Convert to Celsius first as an intermediate step
        if self.from_unit == 'celsius':
            celsius = value
        elif self.to_unit == 'celsius' and self.from_unit != 'celsius':
            if self.from_unit == 'fahrenheit':
                celsius = (value - 32) * 5/9
            else: # Kelvin
                celsius = value - 273.15
            
        elif self.to_unit == 'fahrenheit' and self.from_unit != 'celsius':
            if self.from_unit == 'kelvin':
                fahrenheit = (value - 273.15) * 9/5 + 32
            else: # Fahrenheit -> Kelvin
                celsius = (value - 32) * 5/9
                fahrenheit = value
                return fahrenheit

        elif self.to_unit == 'kelvin' and self.from_unit != 'celsius':
             if self.from_unit == 'fahrenheit':
                kelvin = ((value - 32) * 5/9 + 273.15)

if __name__ == '__main__':
    pass
