class Sensor:
    """Handles reading raw temperature data from a simulated source."""
    
    def read_temperature(self, unit_degrees):
        """
        Simulates reading raw temperature data in Celsius.
        
        Args:
            unit_degrees (str): The input unit string ('c' for celsius or 'f' for fahrenheit).
            
        Returns:
            float: Raw temperature value read from the sensor.
        """
        # Hard-coded sample values to simulate reading data in Celsius and Fahrenheit respectively
        if not isinstance(unit_degrees, str):
            raise ValueError("Unit must be a string.")
        
        raw_data = {
            'c': 25.0,   # Sample value: 25 degrees Celsius
            'f': 77.0    # Sample value: 77 degrees Fahrenheit (which corresponds to ~25 C)
        }
        
        if unit_degrees not in raw_data:
            raise ValueError(f"Unsupported temperature unit '{unit_degrees}'. Supported units are 'c' and 'f'.")
            
        return raw_data[unit_degrees]

class Converter:
    """Handles all necessary unit conversions."""
    
    @staticmethod
    def celsius_to_fahrenheit(celsius_value):
        """Converts Celsius to Fahrenheit."""
        fahrenheit = (celsius_value * 9 / 5) + 32
        return fahrenheit
    
    @staticmethod
    def fahrenheit_to_celsius(fahrenheit_value):
        """Converts Fahrenheit to Celsius."""
        celsius = ((fahrenheit_value - 32) * 5) / 9
        return celsius

if __name__ == '__main__':
    # Demonstrate the Sensor and Converter classes with hard-coded sample values
    
    sensor = Sensor()
    
    try:
        raw_celsius = sensor.read_temperature('c')
        print(f"Raw temperature read (C): {raw_celsius} °C")

        converted_fahrenheit = Converter.celsius_to_fahrenheit(raw_celsius)
        print(f"Converted to Fahrenheit: {converted_fahrenheit:.2f} °F")

    except ValueError as e:
        print(f"Error reading sensor data: {e}")

    try:
        raw_fahrenheit = sensor.read_temperature('f')
        print(f"\nRaw temperature read (F): {raw_fahrenheit} °F")

        converted_celsius = Converter.fahrenheit_to_celsius(raw_fahrenheit)
        print(f"Converted to Celsius: {converted_celsius:.2f} °C")

    except ValueError as e:
        print(f"Error reading sensor data: {e}")