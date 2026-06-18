def compare_volumes(vol1: float, vol2: float) -> tuple[float, float, float]:
    """
    Compare two floating-point volumes and return their ordered values 
    along with the absolute difference.
    
    Args:
        vol1 (float): First volume measurement.
        vol2 (float): Second volume measurement.
        
    Returns:
        tuple[float, float, float]: A tuple containing:
            - The larger of the two volumes
            - The smaller of the two volumes
            - The absolute difference between them
    
    Uses direct comparison for maximum efficiency in Python's built-in types.
    """
    
    if vol1 > vol2:
        large, small = vol1, vol2
    else:
        large, small = vol2, vol1
        
    diff = abs(vol1 - vol2) or 0.0
    
    return (large, small, float(diff))

if __name__ == '__main__':
    # Hard-coded sample values as per constraints
    v_a = 150.75
    v_b = 89.3

    result_large, result_small, result_diff = compare_volumes(v_a, v_b)

    print(f"Larger: {result_large}")       # Larger of the two volumes
    print(f"Smaller: {result_small}")     # Smaller of the two volumes  
    print(f"Difference (abs): {result_diff}  # Absolute difference between them")