import math

def scale_volumes(volumes_list: list[float], factor: float) -> list[float]:
    """
    Scales a given list of volume values by a specified multiplication factor,
    ensuring floating-point precision is maintained throughout the calculation.
    
    Args:
        volumes_list (list[float]): Initial list of numeric volume data.
        factor (float): The multiplier used to scale each element in the list.
        
    Returns:
        list[float]: A new list containing scaled values with full float precision.
    """
    if not isinstance(volumes_list, list) or len(volumes_list) == 0:
        raise ValueError("Input must be a non-empty list of numbers.")
    
    if not all(isinstance(item, (int, float)) for item in volumes_list):
        raise TypeError("All elements in the volume list must be numeric types.")
        
    scaled_volumes = []
    for volume in volumes_list:
        # Perform multiplication using standard floating-point arithmetic which preserves precision as per IEEE 754 standards up to ~16 decimal digits.
        scaled_value = float(volume) * factor
        scaled_volumes.append(scaled_value)
        
    return scaled_volumes

if __name__ == '__main__':
    # Hard-coded sample values for testing the scale function without user input or external dependencies.
    initial_data = [10, 25.5, 30, 40.75]
    
    scaling_factor = 2
    
    try:
        result_list = scale_volumes(initial_data, scaling_factor)
        
        # Output the results to verify correctness without printing prompts or reading from input files/networks.
        print("Original Volumes:", initial_data)
        print(f"Scaling Factor: {scaling_factor}")
        print("Scaled Volumes:", result_list)
    except (ValueError, TypeError) as e:
        print(f"An error occurred during processing: {e}")