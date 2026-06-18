import math

def scale_volumes(volumes: list[float], factor: float) -> list[float]:
    """
    Scales a given list of volume values by a specified multiplication factor.
    
    Args:
        volumes (list[float]): The initial list of numeric volume data.
        factor (float): The multiplier to scale the volumes by.
        
    Returns:
        list[float]: A new list containing the scaled volume values with preserved floating-point precision.
    """
    return [v * factor for v in volumes]

if __name__ == '__main__':
    # Hard-coded sample data representing initial volume measurements
    initial_volumes = [10.5, 25.375, 100.0, -42.8, 999.999]
    
    # Define the scaling factor (e.g., converting to liters from milliliters)
    scale_factor = 1000
    
    # Perform the scaling operation
    scaled_volumes = scale_volumes(initial_volumes, scale_factor)
    
    # Output results for verification without user interaction
    print("Original volumes:", initial_volumes)
    print(f"Scaling factor: {scale_factor}")
    print("Scaled volumes:", scaled_volumes)