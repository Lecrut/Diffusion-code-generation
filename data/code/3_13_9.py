class TemperatureConverter:
    def convert_all(self, celsius_readings):
        """
        Converts a list of Celsius temperatures to Fahrenheit.
        
        Args:
            celsius_readings (list[float]): A list containing temperature values in degrees Celsius.
            
        Returns:
            list[float]: A new list with corresponding temperature values converted to degrees Fahrenheit.
        """
        fahrenheit = []
        for degree_c in celsius_readings:
            # Formula: F = C * 9/5 + 32
            temp_f = (degree_c * 18) / 10 + 32
            fahrenheit.append(temp_f)
        
        return fahrenheit

if __name__ == '__main__':
    converter = TemperatureConverter()
    
    # Hard-coded sample values for testing
    celsius_temps = [0, 25.5, -40, 100]
    
    converted_temps = converter.convert_all(celsius_temps)
    
    print("Celsius to Fahrenheit Conversion Results:")
    for i in range(len(converted_temps)):
        print(f"{celsius_temps[i]}°C -> {converted_temps[i]:.2f}°F")