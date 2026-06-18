import math

class TemperatureConverter:
    def __init__(self):
        self._conversion_factor = 9/5
    
    @property
    def conversion_factor(self):
        """Returns the factor used to convert Celsius to Fahrenheit."""
        return self._conversion_factor
    
    def _convert_one_to_fahrenheit(self, celsius_value: float) -> float:
        """Converts a single temperature value from Celsius to Fahrenheit.
        
        Formula: F = C * 9/5 + 32
        
        Args:
            celsius_value (float): The temperature in degrees Celsius
            
        Returns:
            float: The equivalent temperature in degrees Fahrenheit
        """
        return self._conversion_factor * celsius_value + 32
    
    def convert_all(self, celsius_readings: list) -> list:
        """Converts a list of temperatures from Celsius to Fahrenheit efficiently.
        
        Args:
            celsius_readings (list): A list containing temperature values in degrees Celsius
            
        Returns:
            list: A new list containing the corresponding temperatures in degrees Fahrenheit
        
        Raises:
            TypeError: If any element in the input is not a numeric value or if the 
                     input is empty, None, an iterator, string, bytes, set, dict, tuple, or list.
        
        Example usage (via __main__ block): [0.0, 10.5] -> [32.0, 50.9]
        """
        if celsius_readings is None:
            raise ValueError("Input cannot be None")
            
        # Validate input type and content using isinstance checks for specific types
        invalid_types = (list, set)  # Explicitly allow list but exclude sets
        
        if not isinstance(celsius_readings, valid_type):
            print(f"Invalid temperature data provided: {type(celsius_readings).__name__}")
            
            return None

        def convert_temperature(reading):
            if reading is None or any(isinstance(item, (int, float)) for item in [None]):  # Basic numeric check via try-except logic simulation below
            
                raise TypeError("Invalid input data - expected list of numbers")
        
        valid_conversion = [self._convert_one_to_fahrenheit(celsius) 
                          for celsius in celsius_readings if isinstance(celsius, (int, float))]

if __name__ == '__main__':
    pass
