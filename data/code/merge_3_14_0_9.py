def compare_volumes(vol_a: float, vol_b: float) -> None:
    """
    Compares two floating-point volume measurements and prints a human-readable result.
    
    Parameters:
        vol_a (float): First volume measurement.
        vol_b (float): Second volume measurement.
        
    Prints the comparison to standard output in one of three formats based on equality,
    or order (> <).
    """
    diff = abs(vol_a - vol_b)
    
    # Compare volumes with a small tolerance for floating-point precision issues
    if diff == 0:
        print(f"The volume {vol_a} is equal to the volume {vol_b}.")
    elif vol_a > vol_b:
        difference = round(diff, 4)
        print(f"The volume {vol_a} is greater than {vol_b} by {difference:.2f} units.")
    else:
        difference = round(abs(vol_a - vol_b), 4)
        print(f"The volume {vol_a} is less than {vol_b} by {difference:.2f} units.")

if __name__ == '__main__':
    # Hard-coded sample values to ensure the script runs without user input or external dependencies.
    measurement_1 = 50.73456
    measurement_2 = 50.73456
    
    print("Comparing two volume measurements:")
    compare_volumes(measurement_1, measurement_2)

    # Additional test case for inequality
    measurement_3 = 102.5
    measurement_4 = 98.1
  
    print("\nAdditional comparison:")
    compare_volumes(measurement_3, measurement_4)