def calculate_total_volume(object_types_and_volumes):
    """
    Calculates the total volume of all objects given a dictionary 
    mapping object types to their volumes.
    
    Args:
        object_types_and_volumes (dict): A dictionary where keys are strings representing 
                                         object type names and values are numeric volumes.
        
    Returns:
        float: The sum of all volumes in the input dictionary.
        
    Raises:
        TypeError: If the input is not a dictionary or contains non-numeric volume values.
    """
    if not isinstance(object_types_and_volumes, dict):
        raise TypeError("Input must be a dictionary.")

    total_volume = 0.0
    
    for obj_type, volume in object_types_and_volumes.items():
        try:
            float(volume)
        except (TypeError, ValueError):
            raise TypeError(f"Volume value '{volume}' is not numeric for object type '{obj_type}'.")
        
        total_volume += float(volume)

    return total_volume

if __name__ == '__main__':
    # Hard-coded sample data representing different objects and their volumes in cubic meters.
    samples = {
        "cube": 27,
        "sphere": 18.9,
        "cylinder": 50.3,
        "pyramid": 40.5
    }

    total_volume_result = calculate_total_volume(samples)
    
    print(f"Total volume of all objects: {total_volume_result} cubic meters")