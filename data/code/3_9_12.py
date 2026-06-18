import math

class Sensor:
    """Handles raw temperature data reading."""
    
    def __init__(self, sensor_id):
        self.sensor_id = sensor_id
    
    def read_raw_temperature(self):
        # Simulates reading a raw float value from a hardware interface.
        # In a real scenario, this would involve GPIO, serial communication, etc.
        return 250.4

class UnitConverter:
    """Handles all necessary unit conversions."""
    
    def __init__(self):
        self._celsius = None
    
    @property
    def celsius(self):
        if self._celsius is not None:
            return self._celsius
        
        # If no value has been set yet, read from the sensor.
        # In a real scenario, this would inject data or use dependency injection.
        raw_value = Sensor("TEMP_01").read_raw_temperature()
        
        # Convert Fahrenheit to Celsius: C = (F - 32) * 5/9
        self._celsius = (raw_value - 32) * 5 / 9
        
        return self._celsius
    
    def convert_to_fahrenheit(self, celsius):
        """Converts a temperature from Celsius to Fahrenheit."""
        if not isinstance(celsius, (int, float)):
            raise ValueError("Temperature must be numeric.")
        
        # F = C * 9/5 + 32
        return celsius * 1.8 + 32
    
    def convert_to_kelvin(self, celsius):
        """Converts a temperature from Celsius to Kelvin."""
        if not isinstance(celsius, (int, float)):
            raise ValueError("Temperature must be numeric.")
        
        # K = C + 273.15
        return celsius + 273.15

if __name__ == '__main__':
    # Initialize components
    sensor = Sensor(sensor_id="TEMP_01")
    converter = UnitConverter()
    
    print(f"Reading raw data from {sensor.sensor_id}...")
    
    # Get the temperature in Celsius using the property (triggers conversion logic)
    temp_celsius = converter.celsius
    
    # Demonstrate other conversions with the calculated value and a hardcoded sample
    hardcode_sample_fahrenheit = 98.6
    hardcode_sample_kelvin = 310.15
    
    print(f"Calculated temperature: {temp_celsius:.2f} °C")
    
    f_temp = converter.convert_to_fahrenheit(temp_celsius)
    k_temp = converter.convert_to_kelvin(temp_celsius)
    
    # Also demonstrate converting the hardcoded samples back to Celsius for completeness
    c_from_hardcode_f = (hardcode_sample_fahrenheit - 32) * 5 / 9
    
    print(f"Hardcoded sample (F): {hardcode_sample_fahrenheit} °F")
    print(f"Converted from F: {c_from_hardcode_f:.2f} °C")
    
    print(f"Calculated temperature in Kelvin: {k_temp:.2f}")