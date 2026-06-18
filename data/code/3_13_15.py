class TemperatureConverter:
    """A class to convert temperatures from Celsius to Fahrenheit."""
    
    def __init__(self):
        pass
    
    def convert_all(self, celsius_readings):
        """
        Converts a list of Celsius temperature readings to their corresponding 
        Fahrenheit values.

        Args:
            celsius_readings (list[float]): A list containing numerical values in degrees Celsius.

        Returns:
            list[float]: A new list with the same number of elements, where each element is the 
                        converted value in degrees Fahrenheit.
        
        Formula used: F = C * 9/5 + 32
        
        Example:
            >>> converter = TemperatureConverter()
            >>> result = converter.convert_all([0, 100])
            [32.0, 212.0]
        """
        fahrenheit_readings = []
        
        for celsius in celsius_readings:
            # Apply the conversion formula F = (C * 9/5) + 32
            fahrenheit_value = (celsius * 9 / 5) + 32
            fahrenheit_readings.append(fahrenheit_value)
            
        return fahrenheit_readings

if __name__ == '__main__':
    # Hard-coded sample values for testing without user input or external dependencies
    celsius_temps = [0, 10.5, -40, 36.6]
    
    converter = TemperatureConverter()
    fahrenheit_temps = converter.convert_all(celsius_temps)
    
    print("Celsius to Fahrenheit Conversion Results:")
    for i in range(len(fahrenheit_temps)):
        print(f"{celsius_temps[i]}°C -> {fahrenheit_temps[i]:.2f}°F")