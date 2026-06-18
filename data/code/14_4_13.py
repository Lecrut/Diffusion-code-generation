def compare_volumes(vol_a: float, vol_b: float) -> None:
    """Compare two volume measurements and print their relationship."""
    if vol_a > vol_b:
        print(f"{vol_a} is greater than {vol_b}")
    elif vol_a < vol_b:
        print(f"{vol_a} is less than {vol_b}")
    else:
        print(f"{vol_a} is equal to {vol_b}")

if __name__ == '__main__':
    # Hard-coded sample values as per instructions (no input() or sys.stdin)
    volume_1 = 5.0
    volume_2 = 3.7
    
    compare_volumes(volume_1, volume_2)