def calculate_total_volume(object_types_and_volumes):
    """
    Calculates the total volume of all objects given a dictionary 
    where keys are object types and values are their respective volumes.
    
    Args:
        object_types_and_volumes (dict): A dictionary with object type strings as keys 
                                        and numeric volume measurements as values.
        
    Returns:
        float or int: The sum of all volume measurements.
        
    Raises:
        TypeError: If the input is not a dictionary or if any value is not numeric.
    """
    total_volume = 0
    
    # Validate that input is a dictionary and iterate over items safely
    for obj_type, volume in object_types_and_volumes.items():
        if not isinstance(volume, (int, float)):
            raise TypeError(f"Volume for '{obj_type}' must be numeric. Got {type(volume).__name__}.")
        
        total_volume += volume
        
    return total_volume

if __name__ == '__main__':
    # Hard-coded sample data with various object types and volumes
    objects = {
        "cube": 27,
        "sphere": 36.58,
        "cylinder": 100,
        "box": 48.5
    }

    result_volume = calculate_total_volume(objects)
    
    # Output the calculated total volume directly to stdout
    print(f"Total Volume: {result_volume}")