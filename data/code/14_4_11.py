def compare_volumes(volume1: float, volume2: float) -> str:
    """Compares two numeric volumes and returns a description of their relationship."""
    if volume1 > volume2:
        return f"{volume1} is greater than {volume2}"
    elif volume2 > volume1:
        return f"{volume2} is greater than {volume1}"
    else:
        return f"{volume1} is equal to {volume2}"

if __name__ == '__main__':
    # Hard-coded sample values for demonstration purposes.
    sample_vol_a = 50.0
    sample_vol_b = 75.0
    
    result = compare_volumes(sample_vol_a, sample_vol_b)
    print(f"Comparing {sample_vol_a} and {sample_vol_b}:")
    print(result)