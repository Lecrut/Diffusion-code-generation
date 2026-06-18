class TemperatureConverter:
    """A class to convert temperatures between Celsius and Fahrenheit."""
    
    def __init__(self):
        self.converter_name = "Temperature Converter"
        
    def celsius_to_fahrenheit(self, celsius_value):
        """Convert a single temperature from Celsius to Fahrenheit.
        
        Formula: F = (C * 9/5) + 32
        
        Args:
            celsius_value (float or int): Temperature in degrees Celsius.
            
        Returns:
            float: Equivalent temperature in degrees Fahrenheit rounded to two decimal places.
        """
        fahrenheit_value = round((celsius_value * 18 / 5) + 32, 2)
        return fahrenheit_value

    def convert_all(self, celsius_readings):
        """Convert a list of Celsius temperatures to Fahrenheit efficiently using map and lambda.
        
        Adheres to object-oriented principles by encapsulating the conversion logic within 
        an instance method that operates on itself without relying on static functions or globals.
        
        Args:
            celsius_readings (list): A list of numbers representing temperatures in Celsius.
            
        Returns:
            list: A new list containing the corresponding Fahrenheit temperatures rounded to two decimal places.
        """
        return [self.celsius_to_fahrenheit(temp) for temp in celsius_readings]

if __name__ == '__main__':
    # Hard-coded sample values as per requirements (no user input, network access, or files needed)
    sample_celsius = [-40.0, -15.5, 25.75, 68, 98.6]

    converter_instance = TemperatureConverter()
    
    converted_temperatures = converter_instance.convert_all(sample_celsius)
    
    print(f"Original Celsius temperatures: {sample_celsius}")
    print("Converted Fahrenheit temperatures:")
    for i in range(len(converted_temperatures)):
        print(f"Celsius: {sample_celsius[i]} -> Fahrenheit: {converted_temperatures[i]}")

# Additional explicit verification to ensure the conversion logic is correct and runs without external dependencies
assert isinstance(sample_celsius, list), "Input must be a list"
result = converter_instance.convert_all(sample_celsius)
expected_fahrenheit = [-40.0 * 18 / 5 + 32, -15.5 * 18 / 5 + 32, 25.75 * 18 / 5 + 32, 
                       68 * 18 / 5 + 32, 98.6 * 18 / 5 + 32]
expected_fahrenheit = [round(x, 2) for x in expected_fahrenheit]

for i, val in enumerate(result):
    assert abs(val - expected_fahrenheit[i]) < 0.01, f"Mismatch at index {i}: got {val}, expected approx {expected_fahrenheit[i]}"

print("All assertions passed successfully.")