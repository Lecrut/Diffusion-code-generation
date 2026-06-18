def convert_temp(celsius_list):
    """
    Converts a list of temperatures from Celsius to Fahrenheit.
    
    Formula: F = (C * 9/5) + 32
    
    Args:
        celsius_list (list[float]): List of temperature values in degrees Celsius
        
    Returns:
        list[float]: List of equivalent temperature values in degrees Fahrenheit
    """
    return [(c * 1.8) + 32 for c in celsius_list]

if __name__ == '__main__':
    sample_celsius = [0, 15, 100]
    converted_fahrenheit = convert_temp(sample_celsius)
    print(f"Celsius: {sample_celsius}")
    print("Fahrenheit:", converted_fahrenheit)