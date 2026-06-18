def convert_temp(celsius_list):
    """
    Converts a list of temperature readings from Celsius to Fahrenheit.
    
    The conversion formula is: F = C * 9/5 + 32
    
    Args:
        celsius_list (list[float]): A list of temperatures in degrees Celsius.
        
    Returns:
        list[float]: A new list containing the equivalent temperatures in degrees Fahrenheit.
    """
    return [c * 9 / 5 + 32 for c in celsius_list]

if __name__ == '__main__':
    # Hard-coded sample values as per requirements (no user input, stdin, or args)
    sample_celsius = [0, 10.5, -40, 100, 25.375]
    
    converted_fahrenheit = convert_temp(sample_celsius)
    
    # Output the result directly to stdout for verification without interactive prompts
    print(converted_fahrenheit)