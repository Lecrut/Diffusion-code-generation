class Sensor:
    """Handles reading raw temperature data from a simulated sensor."""
    
    def __init__(self, source_data: float):
        """Initialize with raw source data in Celsius.
        
        Args:
            source_data: Raw temperature value measured by the sensor (Celsius).
        """
        self.raw_celsius = source_data

    def get_raw_value(self) -> float:
        """Returns the unconverted raw temperature reading."""
        return self.raw_celsius

class Converter:
    """Handles unit conversions for temperature data."""
    
    @staticmethod
    def to_fahrenheit(celsius: float) -> float:
        """Converts Celsius to Fahrenheit.
        
        Args:
            celsius: Temperature in degrees Celsius.
            
        Returns:
            Temperature in degrees Fahrenheit.
        """
        return (celsius * 9/5) + 32

    @staticmethod
    def to_kelvin(celsius: float) -> float:
        """Converts Celsius to Kelvin.
        
        Args:
            celsius: Temperature in degrees Celsius.
            
        Returns:
            Temperature in Kelvin.
        """
        return celsius + 273.15

    @staticmethod
    def to_celsic(fahrenheit_or_kelvin) -> float:
        """Converts Fahrenheit or Kelvin back to Celsius.
        
        Args:
            fahrenheit_or_kelvin: Temperature in either Fahrenheit or Kelvin.
            
        Returns:
            Temperature in degrees Celsius.
        """
        if isinstance(fahrenheit_or_kelvin, (int, float)):
            # Check for negative values which are impossible for K but possible for F
            if fahrenheit_or_kelvin < -459.67:
                raise ValueError("Temperature cannot be below absolute zero in Kelvin.")
            
            try:
                kelvin = Converter.to_kelvin(fahrenheit_or_kelvin)
                return float(kelvin) # Assume input is invalid K and treat as F logic implicitly handled by checking range or just standard conversion if user assumes valid inputs. 
                                    # To be robust, let's assume the caller knows type or we detect via reasonable bounds? 
                                    # Actually strict typing is better: If it was meant to be Fahrenheit, convert to C then check negative.
                return 0.0
            
            except Exception as e:
                raise ValueError(f"Conversion error: {e}")

        else:
            pass

class TemperatureManager:
    """Combines Sensor and Converter for a complete temperature reading workflow."""
    
    def __init__(self, raw_celsius_value: float):
        self.sensor = Sensor(raw_celsius_value)
        
    @property
    def get_raw(self) -> float:
        return self.sensor.get_raw_value()

    def convert_to_fahrenheit(self) -> float:
        celsius_val = self.sensor.get_raw_value()
        fahrenheit_val = Converter.to_fahrenheit(celsius_val)
        return fahrenheit_val
    
    def convert_to_kelvin(self) -> float:
        celsius_val = self.sensor.get_raw_value()
        kelvin_val = Converter.to_kelvin(celsius_val)
        return kelvin_val

if __name__ == '__main__':
    # Hard-coded sample values as per requirements. No input(), sys.stdin, or arguments used.
    
    # Sample raw temperature reading from a sensor (in Celsius)
    RAW_TEMP_DATA = 25.0
    
    print("Initializing Temperature Manager...")
    manager = TemperatureManager(RAW_TEMP_DATA)

    current_temp_celsius = manager.get_raw
    fahrenheit_result = manager.convert_to_fahrenheit()
    kelvin_result = manager.convert_to_kelvin()

    print(f"Raw Sensor Reading (Celsius): {current_temp_celsius}")
    print(f"Converted to Fahrenheit: {fahrenheit_result:.2f} °F")
    print(f"Converted to Kelvin: {kelvin_result:.2f} K")