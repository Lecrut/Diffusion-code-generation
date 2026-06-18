def standardize_volume(measurements: dict, conversion_factors: float) -> dict:
    """
    Converts all volume measurements in a dictionary to cubic meters 
    using predefined or provided conversion factors (1 unit = conversion_factor m^3).
    
    Args:
        measurements (dict): Dictionary with material names as keys and volumes 
                            as values. Keys are strings, values can be float or int.
        conversion_factors (float): Conversion factor where 1 input_unit = conversion_factors cubic meters.

    Returns:
        dict: A dictionary containing the converted volumes in cubic meters for each key.
    
    Note:
        The function assumes uniform units across all inputs and applies a single 
        global conversion factor to scale everything to m^3. Users should provide 
        this argument with factors appropriate for their input unit (e.g., 0.0264172 
        if measuring in gallons). If no specific arguments are passed via the function,
        it defaults to assuming inputs represent cubic feet and converts them directly 
        to m^3 using a factor of approximately 0.0283168 (though users should override
        this by passing conversion_factors explicitly for accuracy).

    Raises:
        TypeError: If input is not a dictionary or if any value in the dictionary is unconvertible.
    
    Example Usage:
        # To convert gallons to m^3, call with 0.264172 (since 1 gal ≈ 0.00378541 m³)
        # For this generic example below, we assume input is in cubic meters directly by defaulting factor=1.
    """
    
    if not isinstance(measurements, dict):
        raise TypeError("Input must be a dictionary.")

    standardized_data = {}

    for key, value in measurements.items():
        
        try:
            numeric_value = float(value)
        except (ValueError, TypeError):
            raise ValueError(f"Invalid volume measurement '{key}': expected numeric type.") from None
        
        converted_volume = conversion_factors * numeric_value
        standardized_data[key] = converted_volume

    return standardized_data

if __name__ == '__main__':
    
    # Hard-coded sample values assuming inputs are in gallons and we use 
    # the standard factor: 1 gallon ≈ 0.00378541 m³
    
    input_measurement_dict = {
        'water': 264,       # Approximate bucket size
        'oils': 196,        # Smaller container
        'chemicals': 88      # Another small unit
        
    }

    
# Define conversion factor: converting gallons to cubic meters
    
    gallon_to_cubic_meters = 0.00378541
    
    standardized_measurement_dict = standardize_volume(input_measurement_dict, gallon_to_cubic_meters)
    
print("Standardized Volumes (in m³):")
for item in sorted(standardized_measurement_dict.items()):
    print(f"{item[0]}: {item[1]:.6f}")