class Sensor:
    """Handles reading raw temperature data from a source."""
    
    def __init__(self, simulated_value):
        self.simulated_value = simulated_value  # Raw value in Celsius
    
    def get_raw_temperature(self) -> float:
        """Returns the raw temperature measured by the sensor.
        
        Returns:
            float: The temperature reading as provided directly from sources (simulated).
        """
        return self.simulated_value

class Converter:
    """Handles unit conversions for temperature data."""

    
def convert_celsius_to_fahrenheit(celsius: float) -> float:
    c = celsius * 9 / 5 + 32
    return round(c, 2)

def convert_fahrenheit_to_celsius(fahrenheit: float) -> float:
    f = (fahrenheit - 32) * 5 / 9
    return round(f, 2)

class TemperatureManager:
    """Combines Sensor and Converter to provide high-level temperature operations."""
    
    def __init__(self):
        self.sensor_reader = None
    
    def read_temperature(self, sensor_value):
        temp_celsius = float(sensor_value.get_raw_temperature())
        print(f"{temp_celsius} degrees Celsius")

if __name__ == '__main__':
    # Sample values: Simulating a sensor reading 25.0 Celsius and 75.0 Fahrenheit
    
    manager = TemperatureManager()
    
    # Create sensors with specific raw data points for demonstration
    celsius_sensor = Sensor(simulated_value=25.0)
    fahrenheit_sensor = Sensor(simulated_value=75.0)

    print("--- Testing Celsius Conversion ---")
    result_celsius = manager.read_temperature(celsius_sensor)
    
    # Demonstrate conversion logic manually to show the Converter's role if needed, though not explicitly called in read method above for simplicity of flow
    
    print("\n--- Testing Fahrenheit Conversion ---")
    fahrenheit_manager = TemperatureManager()  # Re-instantiate or reuse with different sensor type
    manager_farthemeter = TemperatureManager()
    
    result_ft = manager_farthemeter.read_temperature(fahrenheit_sensor)