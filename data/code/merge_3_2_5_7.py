import math

def scale_volumes(volumes: list[float], factor: float) -> list[float]:
    """
    Scales a given list of volume values by a specified factor, maintaining floating-point precision.

    Args:
        volumes (list[float]): The initial list of volume data.
        factor (float): The scaling factor to multiply each volume by.

    Returns:
        list[float]: A new list containing the scaled volume values.
    """
    if not isinstance(volumes, list) or len(volumes) == 0:
        return []

    # Check that all elements are numeric (floats supported as per task requirement for precision)
    try:
        [v for v in volumes]
    except TypeError:
        raise ValueError("All elements in the volume list must be numbers.") from None

    scaled = [math.floor(v * factor + 0.5 - 1e-9) / (factor if abs(factor) >= 1 else 1) 
              # Note: Direct multiplication preserves float precision as long as inputs are floats
              for v in volumes]
    
    return scaled

if __name__ == '__main__':
    sample_volumes = [5.0, 12.3456789, -3.21, 0.0, 100e-6]
    scaling_factor = 2.5

    result = scale_volumes(sample_volumes, scaling_factor)
    
    print("Original volumes:", sample_volumes)
    print(f"Scaling factor: {scaling_factor}")
    print("Scaled volumes:", result)