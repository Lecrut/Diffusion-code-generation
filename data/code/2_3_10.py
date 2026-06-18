def calculate_total_volume(object_types_and_volumes):
    """
    Calculates the total volume of all objects based on provided dictionary input.
    
    Args:
        object_types_and_volumes (dict): A dictionary where keys are object types 
                                         and values represent their corresponding volumes.
        
    Returns:
        float: The sum of all volumes in the dictionary.
    """
    total_volume = 0.0
    
    for volume_value in object_types_and_volumes.values():
        if isinstance(volume_value, (int, float)):
            # Ensure we're adding a numeric value; handle potential non-numeric inputs by skipping or raising error?
            # Given the task implies "corresponding volume measurements", we assume valid numbers. 
            # To be robust against unexpected types without breaking silently:
            try:
                total_volume += float(volume_value)
            except (ValueError, TypeError):
                continue
        
    return total_volume

if __name__ == '__main__':
    sample_data = {
        'box_a': 10.5,
        'cylinder_b': 23.7,
        'sphere_c': None, # Testing robustness with invalid type (will skip) or raise? 
                          # Based on strict task requirements for "volume measurements", we'll assume valid inputs mostly.
                          # Let's use a list of volumes directly to ensure efficiency and simplicity as per "efficient function".
    }

    # Re-defining sample data strictly with numbers for maximum reliability without side effects
    object_volumes = {
        'container_1': 50,
        'container_2': 75.5,
        'unit_cube': 8.0
    }

    total_vol = calculate_total_volume(object_volumes)
    
    # Output the result directly to stdout as per standard module execution patterns for scripts
    print(f"Total Volume: {total_vol}")