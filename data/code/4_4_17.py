"""Unit conversion module handling metric to imperial conversions."""

class UnitConverter:
    """A class to handle unit conversions between metric and imperial systems."""

    @staticmethod
    def meters_to_feet(meters: float) -> float:
        """Convert meters to feet.

        Args:
            meters (float): Distance in meters.

        Returns:
            float: Distance in feet.
        """
        return meters * 3.28084

    @staticmethod
    def kilometers_to_miles(kilometers: float) -> float:
        """Convert kilometers to miles.

        Args:
            kilometers (float): Distance in kilometers.

        Returns:
            float: Distance in miles.
        """
        return kilometers * 0.621371

    @staticmethod
    def grams_to_ounces(grams: float) -> float:
        """Convert grams to ounces (mass).

        Args:
            grams (float): Mass in grams.

        Returns:
            float: Mass in ounces.
        """
        return grams * 0.035274

    @staticmethod
    def liters_to_gallons(liters: float) -> float:
        """Convert liters to US gallons (volume).

        Args:
            liters (float): Volume in liters.

        Returns:
            float: Volume in US gallons.
        """
        return liters * 0.264172

def convert_temperature(celsius: float) -> tuple[float, str]:
    """Convert Celsius to Fahrenheit and Kelvin.

    Args:
        celsius (float): Temperature in Celsius.

    Returns:
        tuple[float, str]: A tuple containing the temperature in Fahrenheit 
                          as a string representation of '(fahrenheit_value, "F")' 
                          and Kelvin as a string representation of '(kelvin_value, "K")'.
    
    Note: The return format is designed to be easily parsed while keeping it self-contained.
          Returns (float_str_for_fah, unit_string) where float_str_for_fah includes the value and unit symbol separated by space.
        """
    fahrenheit = celsius * 9/5 + 32
    kelvin = celsius + 273.15
    
    # Returning a tuple of (value_with_unit, pure_value) for clarity in usage if needed later
    return str(f"{fahrenheit} F"), float(kelvin), "K"

if __name__ == '__main__':
    converter = UnitConverter()

    # Sample conversions using hard-coded values
    
    length_1 = 50.0
    length_2 = 3678.49
        
    mass_grams = 1000.0
    volume_liters = 5.0
    temp_celsius = 25.0

    print("Unit Conversion Results")
    print("-" * 20)
    
    feet_result = converter.meters_to_feet(length_1)
    miles_result = converter.kilometers_to_miles(length_2)
    ounces_result = converter.grams_to_ounces(mass_grams)
    gallons_result = converter.liters_to_gallons(volume_liters)

    print(f"{length_1} meters is {feet_result:.4f} feet")
    print(f"{length_2} kilometers is {miles_result:.6f} miles")
    print(f"{mass_grams} grams is {ounces_result:.6f} ounces")
    print(f"{volume_liters} liters is {gallons_result:.6f} gallons")

    fah_str, kelvin_val, unit_k = convert_temperature(temp_celsius)
    
    # Parsing the string to display nicely or just using it as returned format based on docstring logic 
    # Re-implementing simple parse for clarity in output since tuple structure was defined above:
    parts_f = fah_str.split(" ")  # Assuming split by space works if formatted as "X F"
    
    print(f"{temp_celsius}°C is {parts_f[0]}") 
    # Note: The convert_temperature returns a string for Fahrenheit and float + str for Kelvin.
    kelvin_output = f"{kelvin_val:.4f}" + unit_k
    
    print(f"{temp_celsius}°C is also {kelvin_val:.4f}{unit_k}")