def convert_temp(celsius_list: list[float]) -> list[float]:
    """
    Converts a list of temperatures from Celsius to Fahrenheit.
    
    Formula used: F = (C * 9/5) + 32
    
    Args:
        celsius_list (list): A list of floating-point numbers representing 
                            temperature readings in degrees Celsius.
    
    Returns:
        list[float]: A new list containing the equivalent temperatures 
                    in degrees Fahrenheit.
    """
    fahrenheit = [(c * 9 / 5) + 32 for c in celsius_list]
    return fahrenheit

if __name__ == '__main__':
    # Hard-coded sample values as per requirements (no user input, network access, or files)
    sample_celsius_readings = [0.0, 18.5, 37.2, -4.6, 100.0]

    converted_values = convert_temp(sample_celsius_readings)

    # Output results for verification (can be replaced with print if desired, but kept minimal as per efficiency focus)
    result_output = [f"{c}°C -> {f:.2f}°F" for c, f in zip(sample_celsius_readings, converted_values)]
    print(result_output)