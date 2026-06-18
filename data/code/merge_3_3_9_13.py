class Sensor:
    """Handles reading raw temperature data."""
    
    def __init__(self):
        self.raw_temperature = 250.196 # Simulated raw Kelvin value from a mock sensor
        
    def get_raw_data(self) -> float:
        """Returns the unprocessed temperature reading in Kelvin."""
        return self.raw_temperature

class Converter:
    """Handles unit conversions for temperature data."""

    @staticmethod
    def to_celsius(kelvin: float) -> float:
        """Converts a value from Kelvin to Celsius. Formula: C = K - 273.15"""
        return kelvin - 273.15
    
    @staticmethod
    def to_fahrenheit(celsius: float) -> float:
        """Converts a value from Celsius to Fahrenheit. Formula: F = (C * 9/5) + 32"""
        return (celsius * 9 / 5) + 32

if __name__ == '__main__':
    # Initialize the sensor and converter
    my_sensor = Sensor()
    temperature_converter = Converter()

    # Retrieve raw data from the sensor
    k_value = my_sensor.get_raw_data()

    # Perform conversions using the dedicated converter class
    celsius_temp = temperature_converter.to_celsius(k_value)
    fahrenheit_temp = temperature_converter.to_fahrenheit(celsius_temp)

    print(f"Raw Kelvin: {k_value:.2f}")
    print(f"Celsius: {celsius_temp:.2f}°C")
    print(f"Fahrenheit: {fahrenheit_temp:.2f}°F")