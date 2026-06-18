import math

class Sensor:
    """Handles reading raw temperature data in Fahrenheit."""
    
    def __init__(self, sensor_id):
        self.sensor_id = sensor_id
    
    def read_temperature(self):
        # Simulates reading a raw integer value (Fahrenheit) from hardware or simulation
        return 98.6

class Converter:
    """Handles all unit conversions between Fahrenheit and Celsius."""
    
    @staticmethod
    def fahrenheit_to_celsius(fahrenheit_value):
        """Converts temperature from Fahrenheit to Celsius using the formula C = (F - 32) * 5/9"""
        return (fahrenheit_value - 32) * 5 / 9

class TemperatureMonitor:
    """High-level class that uses Sensor and Converter together."""
    
    def __init__(self, sensor_id):
        self.sensor = Sensor(sensor_id)
        self.converter = Converter()
        
    def get_temperature_celsius(self):
        raw_temp = self.sensor.read_temperature()
        celsius_temp = self.converter.fahrenheit_to_celsius(raw_temp)
        return celsius_temp

if __name__ == '__main__':
    # Create a monitor instance with sample sensor ID 101
    monitor = TemperatureMonitor(sensor_id=101)
    
    # Retrieve and print the converted temperature
    temp_celsius = monitor.get_temperature_celsius()
    raw_fahrenheit = monitor.sensor.read_temperature()
    
    print(f"Sensor ID: {monitor.sensor.sensor_id}")
    print(f"Raw Reading (F): {raw_fahrenheit}")
    print(f"Converted Temperature (C): {temp_celsius:.2f}°")