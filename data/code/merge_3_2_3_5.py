def calculate_total_volume(object_types_and_volumes):
    """
    Calculates the total volume of all objects given a dictionary 
    mapping object types to their volumes.

    Args:
        object_types_and_volumes (dict): A dictionary where keys are strings representing object types,
                                         and values represent numeric volume measurements.

    Returns:
        float or int: The sum of all volume measurements.
    
    Raises:
        ValueError: If any value in the input is not a number.
    """
    total_volume = 0
    
    for obj_type, volume in object_types_and_volumes.items():
        if not isinstance(volume, (int, float)):
            raise ValueError(f"Volume for '{obj_type}' must be numeric.")
        total_volume += volume
        
    return total_volume

if __name__ == '__main__':
    # Hard-coded sample data with no user input required
    samples = {
        "cube": 27.0,
        "sphere": 36.5,
        "cylinder": 18.0,
        "pyramid": 45.5
    }

    total_vol = calculate_total_volume(samples)
    print(f"Total volume: {total_vol}")