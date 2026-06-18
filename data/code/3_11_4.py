def convert_temp(celsius_list):
    """
    Converts a list of temperature readings from Celsius to Fahrenheit.
    
    The conversion formula is: F = C * 9/5 + 32
    
    Args:
        celsius_list (list of float|int): List of temperatures in Celsius.
        
    Returns:
        list of float: List of converted temperatures in Fahrenheit.
    """
    return [c * 9 / 5 + 32 for c in celsius_list]

if __name__ == '__main__':
    # Hard-coded sample values without any user input or external dependencies
    sample_celsius = [-10, 0, 25.5, 40.75]
    
    result_fahrenheit = convert_temp(sample_celsius)
    
    print("Celsius:", sample_celsius)
    print("Fahrenheit:", result_fahrenheit)