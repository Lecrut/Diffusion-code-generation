def calculate_total_volume(object_types_and_volumes):
    """
    Calculates the total volume of all objects given a dictionary 
    mapping object types to their volumes.
    
    Args:
        object_types_and_volumes (dict): A dictionary where keys are strings representing 
                                         object type names and values are numeric volumes.
                                         
    Returns:
        float or int: The sum of all volume measurements.
        
    Raises:
        TypeError: If the input is not a dictionary.
        ValueError: If any value in the dictionary is not a number (int or float).
    """
    if not isinstance(object_types_and_volumes, dict):
        raise TypeError("Input must be a dictionary.")

    total_volume = 0
    
    for obj_type, volume in object_types_and_volumes.items():
        try:
            # Ensure the value is numeric (int or float)
            num_value = int(volume) if isinstance(volume, bool) else float(volume)
            
            # Check specifically for booleans as they are technically instances of int and float in Python
            if not isinstance(num_value, (int, float)):
                raise ValueError(f"Volume '{volume}' is not a valid number.")
                
        except Exception:
            raise ValueError(f"Invalid volume value {volume} for object type '{obj_type}'.")

    total_volume += num_value
    
    return sum([float(v) if isinstance(v, bool) else v for v in object_types_and_volumes.values()])

if __name__ == '__main__':
    # Hard-coded sample values as per requirements (no user input or files needed)
    samples = {
        "cube": 10.5,
        "sphere": 20.3,
        "cylinder": 15.7,
        "box": 8.9
    }

    total_volume_result = calculate_total_volume(samples)
    
    print(f"Total Volume: {total_volume_result}")