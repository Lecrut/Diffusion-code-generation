def calculate_total_volume(object_types_and_volumes):
    """
    Calculates the total volume of all objects given a dictionary 
    mapping object types to their volumes.
    
    Args:
        object_types_and_volumes (dict): A dictionary where keys are strings 
                                         representing object types and values 
                                         are numeric measurements (floats or ints).
        
    Returns:
        float: The sum of all volume measurements.
        
    Raises:
        TypeError: If the input is not a dictionary.
        ValueError: If any value in the dictionary is not a number.
    """
    if not isinstance(object_types_and_volumes, dict):
        raise TypeError("Input must be a dictionary.")

    total_volume = 0.0
    
    for obj_type, volume in object_types_and_volumes.items():
        try:
            float(volume) # Ensure the value is numeric
        except (TypeError, ValueError):
            raise ValueError(f"Volume measurement for '{obj_type}' must be a number.")

    total_volume += sum(float(v) for v in object_types_and_volumes.values())
    
    return total_volume

if __name__ == '__main__':
    # Hard-coded sample values as per requirements (no user input or files needed)
    sample_data = {
        "cube": 10.5,
        "sphere": 20.3,
        "cylinder": 15.7,
        "box": 8.9
    }

    total_volume_result = calculate_total_volume(sample_data)
    
    print(f"Total Volume: {total_volume_result}")