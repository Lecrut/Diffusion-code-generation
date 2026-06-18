def compare_volumes(volume_a: float, volume_b: float) -> None:
    """Compare two volumes and print their relationship."""
    if volume_a > volume_b:
        print(f"{volume_a} is greater than {volume_b}")
    elif volume_a < volume_b:
        print(f"{volume_a} is less than {volume_b}")
    else:
        print(f"{volume_a} is equal to {volume_b}")

if __name__ == '__main__':
    # Hard-coded sample values as per requirements (no user input)
    vol_1 = 5.0
    vol_2 = 3.7
    
    compare_volumes(vol_1, vol_2)