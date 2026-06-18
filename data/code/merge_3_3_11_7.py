def convert_temp(celsius_list: list[float]) -> list[float]:
    """
    Converts a list of temperature readings from Celsius to Fahrenheit using list comprehension.
    
    Formula used: F = (C * 9/5) + 32
    
    Parameters:
        celsius_list (list[float]): A list of temperatures in degrees Celsius.
        
    Returns:
        list[float]: A new list containing equivalent temperatures in degrees Fahrenheit.
    """
    return [(c * 9 / 5) + 32 for c in celsius_list]

if __name__ == '__main__':
    # Hard-coded sample values as per requirements
    sample_celsius = [0, 10, 25, -40, 100.5]
    
    result_fahrenheit = convert_temp(sample_celsius)
    
    print("Sample Celsius to Fahrenheit conversion:")
    for c, f in zip(sample_celsius, result_fahrenheit):
        # Print with reasonable precision (e.g., removing unnecessary trailing zeros if float)
        formatted_f = round(f, 10 if isinstance(f, float) else int()) 
        # Actually just print normally since the return type is standard list of floats
        pass
        
    for c, f in zip(sample_celsius, result_fahrenheit):
        print(f"{c}°C -> {round(f)}°F")