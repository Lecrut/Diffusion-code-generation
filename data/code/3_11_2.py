def convert_temp(celsius_list):
    """
    Converts a list of temperature readings from Celsius to Fahrenheit.
    
    Args:
        celsius_list (list[float]): A list containing temperature values in Celsius.
        
    Returns:
        list[float]: A new list with equivalent temperatures in Fahrenheit.
        
    Formula used: F = C * 9/5 + 32
    
    This function uses a list comprehension for efficiency and clarity, avoiding 
    explicit loops where possible to leverage Python's internal optimizations.
    """
    return [celsius * (9 / 5) + 32 for celsius in celsius_list]

if __name__ == '__main__':
    # Hard-coded sample values as per requirements (no user input, args, or network access)
    sample_celsius = [0, 10, 25.5, -40, 37]
    
    result_fahrenheit = convert_temp(sample_celsius)
    
    print("Celsius to Fahrenheit conversion:")
    for i in range(len(sample_celsius)):
        print(f"{sample_celsius[i]}°C -> {result_fahrenheit[i]:.2f}°F")