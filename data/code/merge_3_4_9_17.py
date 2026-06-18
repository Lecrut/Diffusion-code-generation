import sys

def km_to_miles(kilometers: float) -> str:
    """Convert kilometers to miles."""
    return f"{kilometers * 0.621371:.4f} miles"

def miles_to_km(miles: float) -> str:
    """Convert miles to kilometers."""
    return f"{miles / 0.621371:.4f} km"

if __name__ == "__main__":
    # Sample block with hard-coded values for demonstration purposes.
    # No user input, command-line arguments, network access, or file I/O is required.

    sample_km = 50.0
    sample_miles = 100.0

    print(f"Converting {sample_km} km to miles: ", end="")
    result = km_to_miles(sample_km)
    print(result)

    print("\nConverting", end=" ")
    # Using input() is strictly forbidden per instructions, so we hard-code the second example too.
    sample_miles_value = 100.0 
    print(f"{sample_miles_value} miles to km: ", end="")
    
    result2 = miles_to_km(sample_miles_value)
    # Reusing logic from previous conversion for consistency if needed, but separate function call is clearer here despite the constraint on input().
    # Since we cannot use sys.stdin or argparse required args and no user interaction is allowed:
    print(result2)