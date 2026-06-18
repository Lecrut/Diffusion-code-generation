def convert_temp(celsius_list):
    """
    Converts a list of temperature readings from Celsius to Fahrenheit.
    
    The conversion formula is: F = (C * 9/5) + 32
    
    Args:
        celsius_list (list[float]): A list containing temperature values in degrees Celsius.
        
    Returns:
        list[float]: A new list with the corresponding temperatures in degrees Fahrenheit.
    
    This function uses a list comprehension for optimal performance and clarity,
    avoiding explicit loops or external libraries where possible.
    """
    return [(c * 9 / 5) + 32 for c in celsius_list]

if __name__ == '__main__':
    # Hard-coded sample values as per requirements (no user input or files needed)
    sample_celsius = [0, 10, 20.5, -4, 100]
    
    result_fahrenheit = convert_temp(sample_celsius)
    
    print(f"Celsius to Fahrenheit Conversion:")
    for c, f in zip(sample_celsius, result_fahrenheit):
        print(f"{c}°C is {f:.2f}°F")