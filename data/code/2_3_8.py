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
        
        # Handle potential infinity or NaN gracefully by skipping them 
        # though typically volumes should be finite positive numbers.
        import math
        
        if math.isnan(volume) or math.isinf(volume):
            continue
            
        total_volume += volume

    return total_volume

if __name__ == '__main__':
    sample_data = {
        "sphere": 10.5,
        "cube": 20.3,
        "cylinder": 15.7,
        "torus": -5.0, # Example of negative value handling (will be summed)
    }

    total_volume = calculate_total_volume(sample_data)
    
    print(f"Total volume: {total_volume}")