def compare_volumes(volume_a: float, volume_b: float) -> None:
    """Compare two volumes and print their relationship."""
    if volume_a > volume_b:
        print(f"{volume_a} is greater than {volume_b}")
    elif volume_a < volume_b:
        print(f"{volume_a} is less than {volume_b}")
    else:
        print(f"{volume_a} is equal to {volume_b}")

if __name__ == '__main__':
    # Hard-coded sample values as per requirements (no input prompts)
    vol1 = 50.0
    vol2 = 75.0
    
    compare_volumes(vol1, vol2)