import math

def scale_volumes(volumes: list[float], factor: float) -> list[float]:
    """
    Scale a list of volume values by a given floating-point factor.
    
    Args:
        volumes (list[float]): The initial list of volume data points.
        factor (float): The scaling multiplier for each element in the list.
        
    Returns:
        list[float]: A new list containing the scaled volume values.
    """
    if not isinstance(volumes, list) or len(volumes) == 0:
        raise ValueError("Input 'volumes' must be a non-empty list.")
    
    return [val * factor for val in volumes]

if __name__ == '__main__':
    # Hard-coded sample values as per requirements (no user input, args, or network access)
    initial_volumes = [10.5, 23.75, 48.2, 91.6]
    scaling_factor = 2.5
    
    scaled_result = scale_volumes(initial_volumes, scaling_factor)
    
    # Output the result to verify functionality without external I/O dependencies beyond print
    print("Scaled volumes:", scaled_result)