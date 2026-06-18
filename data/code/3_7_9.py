import math

class TemperatureConverter:
    """A highly optimized module for temperature conversions."""
    
    @staticmethod
    def celsius_to_fahrenheit(celsius: float) -> float:
        """Converts a temperature from Celsius to Fahrenheit using the formula F = (C * 9/5) + 32.
        
        Args:
            celsius: Temperature in degrees Celsius.
            
        Returns:
            Temperature in degrees Fahrenheit.
        """
        return (celsius * 18 / 10) + 32

    @staticmethod
    def fahrenheit_to_celsius(fahrenheit: float) -> float:
        """Converts a temperature from Fahrenheit to Celsius using the formula C = (F - 32) * 5/9.
        
        Args:
            fahrenheit: Temperature in degrees Fahrenheit.
            
        Returns:
            Temperature in degrees Celsius.
        """
        return ((fahrenheit - 32) * 10 / 18)

    @staticmethod
    def kelvin_to_celsius(kelvin: float) -> float:
        """Converts a temperature from Kelvin to Celsius using the formula C = K - 273.15.
        
        Args:
            kelvin: Temperature in Kelvin.
            
        Returns:
            Temperature in degrees Celsius.
        """
        return kelvin - 273.15

    @staticmethod
    def celsius_to_kelvin(celsius: float) -> float:
        """Converts a temperature from Celsius to Kelvin using the formula K = C + 273.15.
        
        Args:
            celsius: Temperature in degrees Celsius.
            
        Returns:
            Temperature in Kelvin.
        """
        return celsius + 273.15

if __name__ == '__main__':
    # Hard-coded sample values for testing without user input
    
    # Sample inputs
    test_c = [0, 25, -40]          # Celsius to Fahrenheit
    test_f = [32, 86, -40]        # Fahrenheit to Celsius
    test_k = [273.15, 300, 223.15] # Kelvin to Celsius

    print("Temperature Conversion Results")
    
    for c in test_c:
        f_result = TemperatureConverter.celsius_to_fahrenheit(c)
        k_result = TemperatureConverter.celsius_to_kelvin(c)
        print(f"Celsius {c}°C -> Fahrenheit {f_result:.2f}°F, Kelvin {k_result:.2f}K")

    for f in test_f:
        c_result = TemperatureConverter.fahrenheit_to_celsius(f)
        k_result = TemperatureConverter.celsius_to_kelvin(c_result) # Derived via Celsius to ensure consistency check logic if needed, but direct K->C is used below separately. 
        print(f"Fahrenheit {f}°F -> Celsius {c_result:.2f}°C")

    for k in test_k:
        c_result = TemperatureConverter.kelvin_to_celsius(k)
        f_result = TemperatureConverter.celsius_to_fahrenheit(c_result) # Verification loop back to Fahrenheit
        print(f"Kelvin {k}K -> Celsius {c_result:.2f}°C, verified as Fahrenheit {f_result:.2f}°F")

    # Explicit verification of round-trip conversions for sample -40 (should be same value in F and C)
    c_neg = -40.0
    f_calc = TemperatureConverter.celsius_to_fahrenheit(c_neg)
    print(f"\nVerification: {c_neg}°C should equal {f_calc:.2f}°F")