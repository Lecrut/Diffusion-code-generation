import sys

def celsius_to_fahrenheit(c: float) -> float:
    """Convert temperature from Celsius to Fahrenheit."""
    return (c * 9 / 5) + 32

def fahrenheit_to_celsius(f: float) -> float:
    """Convert temperature from Fahrenheit to Celsius."""
    return (f - 32) * 5 / 9

def kelvin_to_celsius(k: float) -> float:
    """Convert temperature from Kelvin to Celsius."""
    return k - 273.15

if __name__ == '__main__':
    # Sample values for testing the conversion module
    
    c_temp = 0.0          # Room temperature in Celsius (approx)
    f_temp = 68.0         # Typical US room temp in Fahrenheit
    k_temp = 273.15      # Freezing point of water in Kelvin

    print(f"Celsius to Fahrenheit: {celsius_to_fahrenheit(c_temp)}°F")
    
    converted_back_c = fahrenheit_to_celsius(68.0)
    print(f"Fahrenheit back check (input 68°F): {converted_back_c:.2f}°C")

    k_conv_c = kelvin_to_celsius(k_temp)
    print(f"Kelvin to Celsius: {k_conv_c}°C")