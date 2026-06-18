def calculate_total_volume(object_types_and_volumes):
    """
    Calculates the total volume of all objects given a dictionary 
    mapping object types to their volumes.
    
    Args:
        object_types_and_volumes (dict): A dictionary where keys are string/object 
                                          identifiers and values are numeric volumes.
                                          
    Returns:
        float: The sum of all volume measurements.
        
    Raises:
        TypeError: If the input is not a dictionary or contains non-numeric values.
        ValueError: If any value in the dictionary cannot be converted to a number.
    """
    total_volume = 0
    
    if not isinstance(object_types_and_volumes, dict):
        raise TypeError("Input must be a dictionary.")

    for key, volume in object_types_and_volumes.items():
        try:
            numeric_value = float(volume)
            total_volume += numeric_value
        except (ValueError, OverflowError):
            raise ValueError(f"Invalid volume value '{volume}' for key '{key}'.")

    return total_volume

if __name__ == '__main__':
    # Hard-coded sample data representing object types and their volumes in cubic meters
    sample_data = {
        "sphere": 10.5,
        "cube": 25.75,
        "cylinder": 30.0,
        "tetrahedron": 8.42,
        "irregular_polyhedron": 15.6
    }

    total_vol = calculate_total_volume(sample_data)
    
    print(f"Total volume of all objects: {total_vol} cubic meters")