class Sensor:
    """Handles reading raw temperature data from a simulated source."""
    
    def __init__(self, sensor_id):
        self.sensor_id = sensor_id
    
    def read_raw_temperature(self) -> float:
        """Simulates reading raw temperature in Celsius.
        
        Returns:
            float: The raw temperature value in degrees Celsius.
        """
        # Simulating a hardware read with some noise for demonstration
        return 25.0 + (self.sensor_id * 1.5)

class Converter:
    """Handles unit conversions between different temperature scales."""
    
    @staticmethod
    def celsius_to_fahrenheit(celsius: float) -> float:
        """Converts Celsius to Fahrenheit using the formula F = C * 9/5 + 32."""
        return (celsius * 1.8) + 32
    
    @staticmethod
    def fahrenheit_to_celsius(fahrenheit: float) -> float:
        """Converts Fahrenheit to Celsius using the formula C = (F - 32) / 9/5."""
        return ((fahrenheit - 32) * 1.0) / 1.8
    
    @staticmethod
    def celsius_to_kelvin(celsius: float) -> float:
        """Converts Celsius to Kelvin using the formula K = C + 273.15."""
        return celsius + 273.15

if __name__ == '__main__':
    # Hard-coded sample values for demonstration
    
    # Initialize sensors with IDs 0 and 1
    sensor_0 = Sensor(sensor_id=0)
    sensor_1 = Sensor(sensor_id=1)
    
    print("Temperature Reading Report")
    print("-" * 30)
    
    # Read raw data from both sensors
    temp_celsius_sensor_0 = sensor_0.read_raw_temperature()
    temp_celsius_sensor_1 = sensor_1.read_raw_temperature()
    
    print(f"Sensor ID {sensor_0.sensor_id}: Raw Temp (°C) = {temp_celsius_sensor_0}")
    print(f"Sensor ID {sensor_1.sensor_id}: Raw Temp (°C) = {temp_celsius_sensor_1}")
    
    # Perform conversions using the Converter class
    
    # Convert Sensor 0 data to Fahrenheit and Kelvin
    temp_fahrenheit_0 = Converter.celsius_to_fahrenheit(temp_celsius_sensor_0)
    temp_kelvin_0 = Converter.celsius_to_kelvin(temp_celsius_sensor_0)
    
    print(f"Converted (Sensor {sensor_0.sensor_id}):")
    print(f"  Fahrenheit: {temp_fahrenheit_0:.2f}°F")
    print(f"  Kelvin:     {temp_kelvin_0:.2f}K")
    
    # Convert Sensor 1 data to Fahrenheit and Celsius (round trip check)
    temp_fahrenheit_1 = Converter.celsius_to_fahrenheit(temp_celsius_sensor_1)
    temp_back_to_celsius = Converter.fahrenheit_to_celsius(temp_fahrenheit_1)
    
    print(f"Converted (Sensor {sensor_1.sensor_id}):")
    print(f"  Fahrenheit: {temp_fahrenheit_1:.2f}°F")
    print(f"  Back to C:  {temp_back_to_celsius:.4f}°C (Original was {temp_celsius_sensor_1})")
    
    # Demonstrate reverse conversion logic if needed, though not explicitly requested as input/output interaction.
    # Just showing the capability exists within the Converter class structure.