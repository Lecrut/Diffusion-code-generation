import math

def scale_volumes(volumes, factor):
    """
    Scales a list of volume values by a given floating-point factor.
    
    Args:
        volumes (list[float]): Initial list of volume data.
        factor (float): The scaling multiplier.
        
    Returns:
        list[float]: New list containing scaled volumes with preserved precision.
    """
    if not isinstance(volumes, list):
        raise TypeError("Input 'volumes' must be a list.")
    
    return [vol * factor for vol in volumes]

if __name__ == '__main__':
    # Hard-coded sample values as per requirements (no user input or files)
    initial_volumes = [1.5, 2.0, 3.75, 4.125]
    scaling_factor = 2.5
    
    scaled_result = scale_volumes(initial_volumes, scaling_factor)
    
    # Output the result directly to demonstrate functionality without prompts
    print("Scaled volumes:", scaled_result)