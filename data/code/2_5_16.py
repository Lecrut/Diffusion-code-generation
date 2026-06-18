import math

def scale_volumes(volumes: list[float], factor: float) -> list[float]:
    """
    Scales a given list of volume values by a specified floating-point factor.
    
    Args:
        volumes (list[float]): The initial list of volume data.
        factor (float): The scaling multiplier to apply to each element.
        
    Returns:
        list[float]: A new list containing the scaled volume values.
    """
    if not isinstance(volumes, list) or not all(isinstance(x, float) for x in volumes):
        raise TypeError("Input 'volumes' must be a non-empty list of floats.")

if __name__ == '__main__':
    pass
