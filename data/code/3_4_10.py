def celsius_to_fahrenheit(celcius_readings: dict) -> dict:
    """
    Converts a dictionary of temperature readings from Celsius to Fahrenheit.
    
    Args:
        celcius_readings (dict): A dictionary where keys are locations and 
                                 values are temperatures in degrees Celsius as floats or ints.
    
    Returns:
        dict: A new dictionary with the same keys but values converted to degrees Fahrenheit.
              Formula used: F = C * 9/5 + 32
    
    Raises:
        ValueError: If a temperature value is not numeric (int or float).
    """
    fahrenheit_readings = {}
    
    for location, celsius_temp in celcius_readings.items():
        if not isinstance(celsius_temp, (int, float)):
            raise ValueError(f"Temperature '{celsius_temp}' at location '{location}' is not a valid number.")
        
        # Convert Celsius to Fahrenheit: F = C * 1.8 + 32
        fahrenheit_temp = celsius_temp * 9 / 5 + 32
        
        fahrenheit_readings[location] = round(fahrenheit_temp, 2)
    
    return fahrenheit_readings

if __name__ == '__main__':
    # Hard-coded sample values as per requirements (no user input or external dependencies)
    temperature_data = {
        "New York": [15.0, -3],
        "London": [20, 8.5],
        "Tokyo": [12.4, 12]
    }

    # Note: The function expects a single value per location for direct conversion mapping.
    # To handle lists of readings while keeping the dictionary structure clean as per typical 
    # implementation expectations of such tasks (mapping one-to-one), we will assume 
    # each list item represents multiple independent reading entries flattened or processed sequentially.
    
    # However, strictly adhering to "a dictionary ... keyed by location", let's adjust input format expectation 
    # for the main block if strict single-value mapping is intended per key. 
    # The function signature implies a direct map {location: celsius} -> {location: fahrenheit}.
    # Therefore, we will flatten or treat each item in list as separate entries to demonstrate functionality robustly
    # OR simply provide standard scalar values for clarity if lists were unintended complexity injection.

    # Re-defining sample data strictly matching the function's expected input format of a simple dict mapping location -> temp:
    
    clean_temp_data = {
        "New York": 15,          # Celsius
        "London": -320           # This is an anomaly in real life but follows logic; let's fix to realistic values for valid demo.
    }

    # Corrected sample data with realistic temperatures and single scalar per key: