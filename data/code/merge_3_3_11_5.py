def convert_temp(celsius_readings: list[float]) -> list[float]:
    """
    Converts a list of temperatures from Celsius to Fahrenheit.
    
    The conversion formula is F = C * 9/5 + 32.
    This implementation uses a list comprehension for efficiency and conciseness.

    Args:
        celsius_readings (list[float]): A list of floating-point numbers representing 
                                        temperatures in degrees Celsius.

    Returns:
        list[float]: A new list containing the equivalent Fahrenheit readings.
    """
    return [c * 9 / 5 + 32 for c in celsius_readings]

if __name__ == '__main__':
    # Hard-coded sample values to demonstrate functionality without user input or files.
    sample_celsius = [-40, -10, 0, 25, 100]

    converted_fahrenheit = convert_temp(sample_celsius)

    print(f"Celsius: {sample_celsius}")
    print("Fahrenheit:", [round(temp, 2) for temp in converted_fahrenheit])