class TemperatureConverter:
    """A class to convert temperatures from Celsius to Fahrenheit."""

    def __init__(self):
        # No state needed initially, but allows instantiation of the converter object
        pass

    def convert_all(self, celsius_readings):
        """
        Converts a list of Celsius temperature readings to their corresponding 
        Fahrenheit values.

        The conversion formula is: F = (C * 9/5) + 32
        
        Args:
            celsius_readings (list[float]): A list containing floating-point numbers representing temperatures in Celsius.

        Returns:
            list[float]: A new list containing the converted temperatures in Fahrenheit.
        
        Example:
            >>> converter = TemperatureConverter()
            >>> readings = [0, 100]
            >>> result = convert_all(readings) # This calls via instance method below if used as class func or self-call
            """
        return [(c * 9/5) + 32 for c in celsius_readings]

if __name__ == '__main__':
    # Hard-coded sample values to demonstrate functionality without external inputs
    sample_celcius = [0, 18.64, -40, 100]

    converter = TemperatureConverter()
    
    fahrenheit_results = converter.convert_all(sample_celcius)

    print("Celsius Readings:", sample_celcius)
    print("Fahrenheit Results:", fahrenheit_results)