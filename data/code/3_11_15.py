def convert_temp(celsius_readings: list) -> list:
    """
    Converts a list of temperature readings from Celsius to Fahrenheit.
    
    The formula used is F = (C * 9/5) + 32, which can also be written as C * 1.8 + 32.
    This function uses a list comprehension for optimal performance and readability.

    Args:
        celsius_readings (list): A list of floats or ints representing temperatures in Celsius.

    Returns:
        list: A new list containing the equivalent temperatures in Fahrenheit.
    
    Raises:
        TypeError: If the input is not a list.
    """
    if not isinstance(celsius_readings, list):
        raise TypeError("Input must be a list.")
    
    return [temp * 1.8 + 32 for temp in celsius_readings]

if __name__ == '__main__':
    # Hard-coded sample values representing temperatures in Celsius
    celsius_temps = [-40, -5, 0, 25, 100, 37.78]

    # Convert to Fahrenheit and print the results with descriptive output
    fahrenheit_temps = convert_temp(celsius_temps)
    
    for i in range(len(fahrenheit_temps)):
        print(f"{celsius_temps[i]}°C => {fahrenheit_temps[i]:.2f}°F")