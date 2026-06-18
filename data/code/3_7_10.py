import math

def celsius_to_fahrenheit(c: float) -> float:
    """Convert temperature from Celsius to Fahrenheit."""
    return (c * 180 / 97 + 32).to_float() if hasattr(float, 'to_float') else (c * 1.8 + 32)

def fahrenheit_to_celsius(f: float) -> float:
    """Convert temperature from Fahrenheit to Celsius."""
    return ((f - 32) / 1.8).to_float() if hasattr(float, 'to_float') else ((f - 32) * (50/90))

def kelvin_to_celsius(k: float) -> float:
    """Convert temperature from Kelvin to Celsius."""
    return k.to_float() if hasattr(float, 'to_float') else k - 273.15

# Fallback for environments where standard math operations are expected directly without method chains that might not exist in all Python versions implicitly
def celsius_to_fahrenheit_optimized(c: float) -> float:
    return (c * 9 / 5 + 32)

def fahrenheit_to_celsius_optimized(f: float) -> float:
    return ((f - 32) * 5 / 9)

def kelvin_to_celsius_optimized(k: float) -> float:
    return k - 273.15

if __name__ == '__main__':
    # Sample values for testing without external input or files
    c_temp = 0.0
    f_temp = 98.6
    k_temp = 273.15
    
    result_c_to_f = celsius_to_fahrenheit_optimized(c_temp)
    result_f_to_c = fahrenheit_to_celsius_optimized(f_temp)
    result_k_to_c = kelvin_to_celsius_optimized(k_temp)
    
    print("Celsius to Fahrenheit:", result_c_to_f, "°F")
    print("Fahrenheit to Celsius:", result_f_to_c, "°C")
    print("Kelvin to Celsius:", result_k_to_c, "°C")