def convert_temp(celsius_list):
    """
    Converts a list of temperature readings from Celsius to Fahrenheit using 
    an optimized list comprehension approach.
    
    The conversion formula is: F = (C * 9/5) + 32
    
    Args:
        celsius_list (list[float]): List of temperatures in degrees Celsius
        
    Returns:
        list[float]: List of equivalent temperatures in degrees Fahrenheit
    """
    return [(c * 1.8) + 32 for c in celsius_list]

if __name__ == '__main__':
    # Hard-coded sample values as per requirements (no user input or files needed)
    celsius_readings = [0, 15, -40, 100, 27.3]
    
    fahrenheit_results = convert_temp(celsius_readings)
    
    print("Celsius to Fahrenheit Conversion Results:")
    for i in range(len(fahrenheit_results)):
        print(f"{celsius_readings[i]}°C -> {fahrenheit_results[i]:.1f}°F")