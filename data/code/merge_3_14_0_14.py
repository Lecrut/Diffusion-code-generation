def compare_volumes(volume_a: float, volume_b: float) -> None:
    """
    Compares two floating-point number volumes and prints a human-readable result.

    Args:
        volume_a (float): The first volume measurement.
        volume_b (float): The second volume measurement.

    Prints the comparison details including which is larger, the difference, 
    or if they are equal to four decimal places.
    """
    
    # Determine relationship between volumes
    if abs(volume_a - volume_b) < 1e-9:  # Use epsilon for float equality check
        print(f"Volume A ({volume_a:.4f}) is equal to Volume B ({volume_b:.4f}).")
    elif volume_a > volume_b:
        difference = round(volume_a - volume_b, 4)
        print(f"Volume A ({volume_a:.4f}) is greater than Volume B ({volume_b:.4f}) by {difference}.")
    else:
        difference = round(volume_b - volume_a, 4)
        print(f"Volume A ({volume_a:.4f}) is less than Volume B ({volume_b:.4f}) by {difference}.")

if __name__ == '__main__':
    # Hard-coded sample values for demonstration without user input.
    vol_one = 1250.78934
    vol_two = 1250.7896
    
    print("--- Volume Comparison Results ---\n")
    
    compare_volumes(vol_one, vol_two)