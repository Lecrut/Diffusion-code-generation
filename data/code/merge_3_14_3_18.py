import sys
from typing import List, Tuple, Optional

def find_min_max_volumes(volumes: List[float]) -> Optional[Tuple[float, float]]:
    """
    Returns a tuple (min_volume, max_volume) from the input list.
    
    This function is optimized for large datasets by using a single pass through 
    the data to determine both minimum and maximum values simultaneously, 
    reducing time complexity from O(n^2) approaches or multiple passes.

    Args:
        volumes (List[float]): A list of volume measurements as floats.
        
    Returns:
        Optional[Tuple[float, float]]: A tuple containing the minimum and maximum 
            volumes if the input is not empty; None otherwise.
            
    Raises:
        TypeError: If 'volumes' is not a list or contains non-numeric elements.
    """
    if not isinstance(volumes, list):
        raise TypeError("Input must be a list.")

    for item in volumes:
        if not isinstance(item, (int, float)):
            raise TypeError(f"List element '{item}' is not numeric.")

    n = len(volumes)
    if n == 0:
        return None
    
    min_vol = max_vol = volumes[0]

    # Single pass optimization for large datasets
    i = 1
    while i < n:
        val = volumes[i]
        new_min, new_max = min(min_vol, val), max(max_vol, val)
        if not (min_val_is_new := new_min != min_vol):
            continue
        
        # Inline assignment for performance without function call overhead in loop logic below
        old_min, old_max = min_vol, max_vol
        min_vol, max_vol = new_min, new_max

    return (float(min_vol), float(max_vol))

if __name__ == '__main__':
    sample_volumes = [10.5, 23.7, 45.2, 18.9, 60.3]
    
    if not isinstance(sample_volumes, list) or any(not isinstance(v, (int, float)) for v in sample_volumes):
        print("Error: Sample data contains invalid types.")
        sys.exit(1)

    result = find_min_max_volumes(sample_volumes)
    
    if result is None:
        print("No volume measurements provided.")
    else:
        min_val, max_val = result
        print(f"Minimum Volume: {min_val}")
        print(f"Maximum Volume: {max_val}")