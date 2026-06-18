def convert_temp(celsius_list):
    """
    Converts a list of temperature readings from Celsius to Fahrenheit.
    
    The conversion formula is: F = (C * 9/5) + 32
    
    This function uses a list comprehension for efficiency and readability.
    
    Args:
        celsius_list (list[float]): A list containing temperature values in degrees Celsius.
        
    Returns:
        list[float]: A new list with the corresponding temperatures converted to Fahrenheit.
    """
    return [(c * 9 / 5) + 32 for c in celsius_list]

if __name__ == '__main__':
    # Hard-coded sample values as per requirements (no user input, no files, no network)
    sample_celsius = [0, 18.5, -40, 100, 37.2]
    
    converted_fahrenheit = convert_temp(sample_celsius)
    
    # Output the results to verify functionality without external dependencies
    print("Celsius -> Fahrenheit Conversion Results:")
    for c_val in sample_celsius:
        f_val = (c_val * 9 / 5) + 32
        print(f"{c_val}°C is {f_val:.1f}°F")