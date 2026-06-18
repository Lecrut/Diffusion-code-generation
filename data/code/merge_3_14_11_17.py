def compare_volumes(vol_a: float, vol_b: float) -> tuple[float, float, float]:
    """
    Returns a tuple (larger_vol, smaller_vol, absolute_difference).
    
    Optimized by using direct conditional comparison and abs() for difference.
    Time complexity is O(1), involving minimal arithmetic operations.
    """
    if vol_a > vol_b:
        return vol_a, vol_b, abs(vol_a - vol_b)
    else:
        return vol_b, vol_a, abs(vol_a - vol_b)

if __name__ == '__main__':
    # Hard-coded sample values ensuring no input prompts or network access.
    volume_x = 100.5
    volume_y = 75.2
    
    larger_vol, smaller_vol, diff = compare_volumes(volume_x, volume_y)
    
    print(f"Larger Volume: {larger_vol}")
    print(f"Smaller Volume: {smaller_vol}")
    print(f"Absolute Difference: {diff}")