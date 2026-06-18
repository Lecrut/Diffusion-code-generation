class Sensor:
    """Handles reading raw temperature data from a sensor."""
    
    def __init__(self, sensor_id):
        self.sensor_id = sensor_id
    
    def read_raw_temperature(self) -> float:
        """Simulates reading raw Fahrenheit temperature data.
        
        Returns:
            A float representing the temperature in Fahrenheit.
        """
        # Simulated raw value from hardware/middleware
        return 98.6

class Converter:
    """Handles all necessary unit conversions."""
    
    @staticmethod
    def fahrenheit_to_celsius(fahrenheit: float) -> float:
        """Converts temperature from Fahrenheit to Celsius.
        
        Args:
            fahrenheit: Temperature value in degrees Fahrenheit.
            
        Returns:
            Temperature converted to degrees Celsius.
        """
        return (fahrenheit - 32) * 5 / 9

    @staticmethod
    def celsius_to_fahrenheit(celsius: float) -> float:
        """Converts temperature from Celsius back to Fahrenheit.
        
        Args:
            celsius: Temperature value in degrees Celsius.
            
        Returns:
            Temperature converted to degrees Fahrenheit.
        """
        return (celsius * 9 / 5) + 32

def main():
    # Initialize sensor and converter instances
    temp_sensor = Sensor(sensor_id="TH-001")
    unit_converter = Converter()
    
    # Read raw data from the simulated sensor
    fahrenheit_reading = temp_sensor.read_raw_temperature()
    
    # Convert to Celsius
    celsius_value = unit_converter.fahrenheit_to_celsius(fahrenheit_reading)
    
    print(f"Raw Sensor ID: {temp_sensor.sensor_id}")
    print(f"Temperature (Fahrenheit): {fahrenheit_reading}°F")
    print(f"Temperature (Celsius):  {celsius_value:.2f}°C")

if __name__ == '__main__':
    main()