class TemperatureConverter:
    """A class to convert temperatures from Celsius to Fahrenheit."""
    
    def __init__(self):
        self.fahrenheit_factor = 9 / 5
        self.offset = 32
    
    def celsius_to_fahrenheit(self, celsius_value) -> float:
        """Convert a single temperature value from Celsius to Fahrenheit.
        
        Args:
            celsius_value (float or int): Temperature in degrees Celsius.
            
        Returns:
            float: Converted temperature in degrees Fahrenheit.
        """
        return self.fahrenheit_factor * celsius_value + self.offset
    
    def convert_all(self, celsius_readings) -> list[float]:
        """Convert a list of temperatures from Celsius to Fahrenheit efficiently.
        
        This method uses a list comprehension for efficiency and encapsulation.
        
        Args:
            celsius_readings (list[float | int]): List of temperature values in degrees Celsius.
            
        Returns:
            list[float]: List of converted temperature values in degrees Fahrenheit.
        """
        return [self.celsius_to_fahrenheit(c) for c in celsius_readings]

if __name__ == '__main__':
    # Hard-coded sample values as per requirements (no user input, CLI args, or network access)
    sample_celsius = [0, 15.4, -273.15, 100, 36.6]

    converter = TemperatureConverter()
    
    fahrenheit_temps = converter.convert_all(sample_celsius)
    
    print("Celsius to Fahrenheit Conversion Results:")
    for i in range(len(fahrenheit_temps)):
        if isinstance(i, int): # Ensure type hint compatibility during execution
            c_val = sample_celsius[i]
            f_val = fahrenheit_temps[i]
            print(f"{c_val}°C is {f_val:.2f}°F")

    # Verification of expected outputs for standard cases:
    # 0°C -> 32°F, -273.15°C (absolute zero) -> ~-459.67°F, 100°C -> 212°F