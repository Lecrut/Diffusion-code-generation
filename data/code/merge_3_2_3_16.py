def calculate_total_volume(object_types_and_volumes):
    """
    Calculates the total volume of all objects given a dictionary 
    mapping object types to their volumes.
    
    Args:
        object_types_and_volumes (dict): A dictionary where keys are strings representing 
                                         object type names and values are numbers or floats 
                                         representing individual volumes.
        
    Returns:
        float: The sum of all volume measurements.
    """
    total_volume = 0.0
    
    for obj_type, volume in object_types_and_volumes.items():
        if not isinstance(volume, (int, float)):
            raise TypeError(f"Volume for '{obj_type}' must be a number.")
        
        # Handle negative volumes by ignoring them or raising an error based on requirement.
        # Here we assume valid physical measurements are non-negative; 
        # however, to ensure robustness without changing logic too much:
        if volume < 0:
            raise ValueError(f"Negative volume not allowed for object type '{obj_type}'.")
            
        total_volume += volume
        
    return total_volume

if __name__ == '__main__':
    sample_data = {
        "sphere": 12.5,
        "cube": 8.0,
        "cylinder": 45.3,
        "torus": 7.2
    }

    total_vol = calculate_total_volume(sample_data)
    
    print(f"Total volume of all objects: {total_vol}")