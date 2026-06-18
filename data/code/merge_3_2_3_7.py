def calculate_total_volume(object_types_and_volumes):
    """
    Calculates the total volume of all objects given a dictionary 
    mapping object types to their volumes.

    Args:
        object_types_and_volumes (dict): A dictionary where keys are string 
            representations of object types and values are numeric volumes.

    Returns:
        float: The sum of all volumes in the input dictionary.
    
    Raises:
        TypeError: If the input is not a dictionary or contains non-numeric values.
    """
    if not isinstance(object_types_and_volumes, dict):
        raise TypeError("Input must be a dictionary.")

    total_volume = 0.0
    
    for obj_type, volume in object_types_and_volumes.items():
        try:
            float(volume)
        except (TypeError, ValueError):
            raise TypeError(f"Volume value '{volume}' for type '{obj_type}' is not numeric.")
        
        total_volume += float(volume)

    return total_volume

if __name__ == '__main__':
    # Hard-coded sample data representing object types and their volumes
    sample_data = {
        "cube": 10.5,
        "sphere": 23.7,
        "cylinder": 45.2,
        "pyramid": 8.9
    }

    total_vol = calculate_total_volume(sample_data)
    
    print(f"Total volume of all objects: {total_vol}")