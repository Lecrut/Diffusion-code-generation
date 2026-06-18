def compare_volumes(volume_a: float, volume_b: float) -> None:
    """
    Compares two floating-point numbers representing volumes 
    and prints a human-readable result indicating which is larger or if they are equal.
    
    Parameters:
        volume_a (float): The first volume measurement.
        volume_b (float): The second volume measurement.
        
    Returns:
        None
    
    Example usage:
        compare_volumes(5.0, 10.0) 
        # Output: Volume A is smaller than Volume B by -5.0 units.
    """
    
    difference = volume_a - volume_b
    
    if abs(difference) < 1e-9:  # Using a small epsilon for float comparison safety
        print(f"Volume A ({volume_a}) and Volume B ({volume_b}) are equal.")
    elif difference > 0:
        print(f"Volume A ({volume_a}) is larger than Volume B ({volume_b}).")
        print(f"Their difference is {difference:.2f}.")
    else:
        print(f"Volume A ({volume_a}) is smaller than Volume B ({volume_b}).")
        print(f"Their difference is {-difference:.2f} (absolute value).")

if __name__ == '__main__':
    # Hard-coded sample values for testing without user input or external dependencies.
    vol_1 = 3.5
    vol_2 = 7.8
    
    compare_volumes(vol_1, vol_2)