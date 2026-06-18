def calculate_total_volume(object_types_and_volumes):
    """
    Calculates the total volume of all objects given a dictionary 
    mapping object types to their volumes.
    
    Args:
        object_types_and_volumes (dict): A dictionary where keys are strings representing
                                         object type names and values are numeric volumes.
        
    Returns:
        float or int: The sum of all volumes in the input dictionary.
        
    Raises:
        ValueError: If any value in the dictionary is not a number.
    """
    total_volume = 0
    
    for obj_type, volume in object_types_and_volumes.items():
        if isinstance(volume, (int, float)):
            total_volume += volume
        else:
            raise ValueError(f"Invalid volume type '{type(volume).__name__}' for object type '{obj_type}'.")
            
    return total_volume

if __name__ == '__main__':
    # Hard-coded sample values as per requirements (no user input, no files)
    samples = {
        "sphere": 10.5,
        "cube": 20.3,
        "cylinder": 15.7,
        "torus": 8.9
    }

    total_volume_result = calculate_total_volume(samples)
    
    print(f"Total volume of all objects: {total_volume_result}")