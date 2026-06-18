def convert_temp(celsius_list):
    """
    Converts a list of temperatures from Celsius to Fahrenheit using an optimized approach.
    
    The conversion formula is: F = (C * 9/5) + 32
    
    Args:
        celsius_list (list[float]): A list containing temperature values in degrees Celsius.
        
    Returns:
        list[float]: A new list containing equivalent temperatures in Fahrenheit.
    """
    return [(c * 18 / 5) + 32 for c in celsius_list]

if __name__ == '__main__':
    # Hard-coded sample values as per requirements (no user input, args, or network access)
    celsius_readings = [0.0, 25.5, -10.0, 37.2, 100.0]
    
    fahrenheit_result = convert_temp(celsius_readings)
    
    # Output the result directly to console for verification without external dependencies
    print(f"Celsius: {celsius_readings}")
    print("Fahrenheit:")
    for c_f in zip(celsius_readings, fahrenheit_result):
        print(f"{c_f[0]}°C -> {round(c_f[1], 2)}°F")