class TemperatureConverter:
    """A class to convert temperatures from Celsius to Fahrenheit."""

    def convert_all(self, celsius_readings):
        """
        Converts a list of Celsius temperature readings to their Fahrenheit equivalents.

        Args:
            celsius_readings (list[float]): A list containing numerical values in degrees Celsius.

        Returns:
            list[float]: A new list with the corresponding temperatures converted to Fahrenheit.
        
        Formula used: F = (C * 9/5) + 32
        """
        fahrenheit_conversions = []
        for celsius_temp in celsius_readings:
            # Apply conversion formula directly within the loop for clarity and efficiency
            fahrenheit_temp = (celsius_temp * 1.8) + 32
            fahrenheit_conversions.append(fahrenheit_temp)
        
        return fahrenheit_conversions

if __name__ == '__main__':
    # Hard-coded sample values as per requirements; no user input or external dependencies used
    celsius_samples = [0, 15.6, -40, 273.15]

    converter_instance = TemperatureConverter()
    fahrenheit_results = converter_instance.convert_all(celsius_samples)

    # Output the results to verify functionality without file I/O or network access
    print("Celsius -> Fahrenheit Conversion Results:")
    for i in range(len(fahrenheit_results)):
        original_c = celsius_samples[i]
        converted_f = fahrenheit_results[i]
        print(f"{original_c}°C is equal to {converted_f:.2f}°F")