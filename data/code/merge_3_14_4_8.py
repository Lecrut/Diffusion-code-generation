def compare_volumes(vol_a: float, vol_b: float) -> None:
    """Compare two volume measurements using conditional statements."""
    
    if vol_a > vol_b:
        print(f"{vol_a} is greater than {vol_b}")
    elif vol_a < vol_b:
        print(f"{vol_a} is less than {vol_b}")
    else:
        print(f"{vol_a} is equal to {vol_b}")

if __name__ == '__main__':
    # Hard-coded sample values as per task requirements.
    # No user input, command-line arguments, or network access used here.
    volume_1 = 50.0
    volume_2 = 75.0
    
    compare_volumes(volume_1, volume_2)