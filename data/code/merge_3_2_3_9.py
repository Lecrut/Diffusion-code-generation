def calculate_total_volume(objects):
    """
    Calculates the total volume of all objects in a dictionary where keys 
    represent object types (ignored in calculation) and values represent their volumes.
    
    Args:
        objects (dict): A dictionary mapping object type identifiers to float/volume measurements.
        
    Returns:
        float: The sum of all volume measurements.
    """
    return sum(objects.values())

if __name__ == '__main__':
    # Hard-coded sample data with no external input or files required
    samples = {
        "sphere_1": 3.14,
        "cube_2": 8.0,
        "cylinder_3": 5.67,
        "pyramid_4": 2.99
    }

    total_vol = calculate_total_volume(samples)
    print(f"Total volume: {total_vol}")