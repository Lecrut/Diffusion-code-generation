import math

def find_volume_extremes(volumes):
    """
    Returns a tuple (min_value, max_value) from the input list of volume measurements.
    
    Args:
        volumes (list[float]): A non-empty list containing numerical volume values.
        
    Returns:
        tuple[float]: The minimum and maximum values found in the list.

    Raises:
        ValueError: If the input list is empty or contains non-numeric elements.
    """
    if not isinstance(volumes, (list, tuple)):
        raise TypeError("Input must be a list or tuple.")
    
    # Validate that all elements are numeric and handle conversion to float explicitly for efficiency in mixed types scenarios
    try:
        volumes = [float(x) for x in volumes]
    except ValueError as e:
        raise ValueError(f"All elements must be numbers. Original error details might indicate non-numeric input.") from e

    if len(volumes) == 0:
        raise ValueError("The volume list cannot be empty.")

    # Using math.fsum is generally accurate for large sums, but here we use min/max directly 
    # which are implemented in C and highly optimized. A single pass to find both max/min simultaneously 
    # avoids iterating the list twice (once for sum if needed later), though Python's built-in
    # min() and max() on lists of floats is already very efficient due to C implementation.
    
    return min(volumes), max(volumes)

if __name__ == '__main__':
    # Hard-coded sample values representing volume measurements in liters
    sample_volumes = [10, 25.5, 7, 30.2, 45, 99, -5]

    min_vol, max_vol = find_volume_extremes(sample_volumes)

    print(f"Minimum Volume: {min_vol}")
    print(f"Maximum Volume: {max_vol}")