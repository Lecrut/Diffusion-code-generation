class Sensor:
    """Handles reading raw temperature data from a simulated source."""
    
    def __init__(self, sensor_id):
        self.sensor_id = sensor_id
    
    def read_raw_temperature(self) -> float:
        """Simulates reading raw temperature in Fahrenheit.
        
        Returns:
            float: The raw temperature value in degrees Fahrenheit.
        """
        # Simulating a hardware readout that returns values in Fahrenheit
        return 98.6

class Converter:
    """Handles all necessary unit conversions for temperature data."""
    
    def __init__(self):
        pass
    
    def fahrenheit_to_celsius(self, temp_f) -> float:
        """Converts a temperature from Fahrenheit to Celsius.
        
        Args:
            temp_f (float): Temperature in Fahrenheit.
            
        Returns:
            float: Temperature in Celsius.
        """
        return (temp_f - 32) * 5 / 9
    
    def fahrenheit_to_kelvin(self, temp_f) -> float:
        """Converts a temperature from Fahrenheit to Kelvin.
        
        Args:
            temp_f (float): Temperature in Fahrenheit.
            
        Returns:
            float: Temperature in Kelvin.
        """
        return (temp_f + 459.67) * 5 / 9

def main():
    # Initialize components with hard-coded sample values simulation
    sensor = Sensor(sensor_id="TEMP_001")
    converter = Converter()
    
    raw_temp = sensor.read_raw_temperature()
    
    print(f"Raw Temperature (Fahrenheit): {raw_temp}°F")
    
    celsius_temp = converter.fahrenheit_to_celsius(raw_temp)
    kelvin_temp = converter.fahrenheit_to_kelvin(raw_temp)
    
    print(f"Celsius: {celsius_temp:.2f}°C")
    print(f"Kelvin: {kelvin_temp:.2f} K")

if __name__ == '__main__':
    main()