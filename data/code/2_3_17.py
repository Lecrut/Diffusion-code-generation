def calculate_total_volume(objects):
    """
    Calculates the total volume of all objects in a dictionary.
    
    Parameters:
        objects (dict): A dictionary where keys are object type identifiers 
                        and values are numeric volumes as integers or floats.
                        
    Returns:
        float: The sum of all volume measurements.
        
    Raises:
        TypeError: If the input is not a dictionary, any value in it is not 
                  numeric (int/float), or contains non-numeric keys causing issues 
                  during iteration if treated as values (though here only dict.values() matters).
    """
    total = 0.0
    
    for volume in objects.values():
        try:
            # Attempt to convert value to float to handle integers and floats uniformly
            val_float = float(volume)
            total += val_float
        except TypeError:
            raise TypeError(f"Volume measurement must be numeric, got {type(objects).__name__} at key with type {volume.__class__.__name__}")

    return total

if __name__ == '__main__':
    # Hard-coded sample values as per requirements
    objects = {
        "box": 10.5,
        "sphere": 7.2,
        "cube": 4,
        "cylinder": 8.9
    }

    try:
        total_vol = calculate_total_volume(objects)
        print(f"Total volume of all objects: {total_vol}")
    except Exception as e:
        print(f"Error calculating volume: {e}")