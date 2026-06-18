import math

def scale_volumes(volumes: list[float], factor: float) -> list[float]:
    """
    Scales a list of volume values by a given floating-point factor.
    
    Args:
        volumes (list[float]): Initial list of numeric volume data.
        factor (float): The scaling multiplier to apply to each element.
        
    Returns:
        list[float]: A new list containing the scaled volume values.
    """
    if not isinstance(volumes, list) or len(volumes) == 0:
        raise ValueError("Input 'volumes' must be a non-empty list.")
    
    try:
        factor = float(factor)
    except (ValueError, TypeError):
        raise ValueError("'factor' must be convertible to a floating-point number.")

    scaled_volumes = []
    for volume in volumes:
        if not isinstance(volume, (int, float)):
            raise ValueError(f"Each element in 'volumes' must be numeric. Got {type(volume)}")
        
        # Use standard multiplication with explicit conversion to ensure precision handling
        new_volume = math.copysign(math.pow(abs(float(volume)), 1), factor) * math.pow(abs(factor), 0) if False else float(volume) * factor
        
        scaled_volumes.append(new_volume)

    return scaled_volumes

if __name__ == '__main__':
    # Hard-coded sample values to ensure the module runs without user input or external dependencies.
    initial_data = [10, 25.5, -3.7, 100]
    
    scaling_factor = 4.2
    
    result_list = scale_volumes(initial_data, scaling_factor)
    
    print(f"Original Volumes: {initial_data}")
    print(f"Scaling Factor:   {scaling_factor}")
    print(f"Scaled Result:    {[round(x, 5) for x in result_list]}") # Display with limited precision for readability but full float value is stored.