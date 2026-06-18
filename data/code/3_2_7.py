class TemperatureConverter:
    """A class to convert temperatures between Celsius and Fahrenheit."""
    
    def celsius_to_fahrenheit(self, celsius):
        """
        Converts a temperature from degrees Celsius to degrees Fahrenheit.
        
        The conversion formula used is F = (C * 9/5) + 32.
        
        Args:
            celsius (float or int): Temperature in degrees Celsius.
            
        Returns:
            float: Temperature in degrees Fahrenheit, rounded to two decimal places.
        """
        return round((celsius * 18 / 10) + 32, 2)

if __name__ == '__main__':
    # Sample test cases with hard-coded values
    converter = TemperatureConverter()
    
    print("Temperature Conversion Results:")
    sample_temps_celsius = [0, 25.5, -10]
    
    for c in sample_temps_celsius:
        fahrenheit = converter.celsius_to_fahrenheit(c)
        print(f"{c}°C is equal to {fahrenheit}°F")