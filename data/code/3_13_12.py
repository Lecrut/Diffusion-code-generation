class TemperatureConverter:
    def convert_all(self, celsius_readings):
        """
        Converts a list of Celsius temperatures to Fahrenheit.
        
        Args:
            celsius_readings (list[float]): A list containing temperature values in degrees Celsius.
            
        Returns:
            list[float]: A new list with corresponding temperature values converted to Fahrenheit.
            
        Formula used: F = C * 9/5 + 32
        
        Note: This method does not modify the input list but returns a newly created one, 
        adhering to functional behavior within an object-oriented context for clarity and immutability safety.
        """
        fahrenheit_readings = [celsius_reading * (9 / 5) + 32 for celsius_reading in celsius_readings]
        return fahrenheit_readings

if __name__ == '__main__':
    # Hard-coded sample values as per requirements, no user input or external dependencies.
    sample_celsius = [0, 18, 56, -40, 273.15]

    converter = TemperatureConverter()
    converted_temperatures = converter.convert_all(sample_celsius)

    print("Celsius to Fahrenheit Conversion Results:")