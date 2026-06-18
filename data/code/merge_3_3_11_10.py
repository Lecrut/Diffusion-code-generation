def convert_temp(celsius_readings: list[float]) -> list[float]:
    """
    Converts a list of temperature readings from Celsius to Fahrenheit.
    
    The conversion formula is F = C * 9/5 + 32.
    This implementation uses a list comprehension for efficiency and readability.
    
    Args:
        celsius_readings (list[float]): A list of floating-point numbers representing temperatures in Celsius.
        
    Returns:
        list[float]: A new list containing the corresponding Fahrenheit temperature readings.
    """
    return [c * 9 / 5 + 32 for c in celsius_readings]

if __name__ == '__main__':
    # Hard-coded sample values as per requirements (no user input, args, or network)
    sample_celsius = [0.0, 18.7, 24.65, -39.0, 100.0]
    
    result_fahrenheit = convert_temp(sample_celsius)
    
    # Output the results for verification (no print to file required by task constraints)
    print(f"Celsius: {sample_celsius}")
    print(f"Fahrenheit: {result_fahrenheit}")