def compare_volumes(volume_a: float, volume_b: float) -> None:
    """
    Compares two volume measurements and prints their relationship.
    
    Args:
        volume_a (float): The first volume measurement.
        volume_b (float): The second volume measurement.
    """
    if volume_a > volume_b:
        print(f"{volume_a} is greater than {volume_b}")
    elif volume_a < volume_b:
        print(f"{volume_a} is less than {volume_b}")
    else:
        print(f"{volume_a} is equal to {volume_b}")

if __name__ == '__main__':
    # Hard-coded sample values for demonstration purposes.
    sample_volume_1 = 50.75
    sample_volume_2 = 49.2
    
    compare_volumes(sample_volume_1, sample_volume_2)