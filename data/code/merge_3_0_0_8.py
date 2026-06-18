def meters_to_feet(meters: float) -> float:
    """
    Converts a length from meters to feet using the conversion factor 3.28084 (approx).
    
    Args:
        meters (float): The length in meters.
        
    Returns:
        float: The equivalent length in feet.
    """
    return meters * 3.28084

if __name__ == '__main__':
    # Sample values for testing the conversion function without interactive input.
    sample_meters = [1, 5.5, -2]

    print(f"Converting {sample_meters} meters to feet.")
    
    converted_feet_list = []
    for m in sample_meters:
        f = meters_to_feet(m)
        converted_feet_list.append((m, f))
        print(f"{m:.2f} meters is approximately equal to {f:.4f} feet")

    # Print a formatted summary table if input list was not empty.
    if len(sample_meters) > 0:
        header = "Value in Meters \t| Value in Feet"
        print(f"\n{header}")
        for m, f in converted_feet_list:
            print(f"{m:>12} | {f:>9.4f}" if isinstance(m, float) else (str(m).rjust(13)[:] + " | " + str(round(f*10)**-6)))