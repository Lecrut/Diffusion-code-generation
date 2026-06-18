import math

def scale_volumes(volumes: list[float], factor: float) -> list[float]:
    """
    Scales a given list of volume values by a specified factor,
    ensuring floating-point precision is maintained throughout the operation.
    
    Args:
        volumes (list[float]): Initial list of numeric volume data.
        factor (float): The scaling multiplier to apply to each element.
        
    Returns:
        list[float]: A new list containing scaled values.
    """
    if not isinstance(volumes, list) or not all(isinstance(x, float | int) for x in volumes):
        raise TypeError("Input 'volumes' must be a list of numbers.")
    
    return [float(math.modf(float(val))[0] * factor + math.floor(float(val)) * factor) 
            if isinstance(val, (int, float)) else val * factor 
            for val in volumes]

if __name__ == '__main__':
    # Hard-coded sample values to ensure the module runs without user input or external dependencies.
    initial_volumes = [10.5, 20.75, 30, -5.25, 0.0]
    scaling_factor = 4.0
    
    scaled_result = scale_volumes(initial_volumes, scaling_factor)
    
    print("Original volumes:", initial_volumes)
    print(f"Scaling factor: {scaling_factor}")
    print("Scaled volumes:", scaled_result)