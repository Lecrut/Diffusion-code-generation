def compare_volumes(volume1: float, volume2: float) -> str:
    if not isinstance(volume1, (int, float)) or not isinstance(volume2, (int, float)):
        raise ValueError("Both volumes must be numbers.")
    
    if volume1 > volume2:
        return "Volume 1 is greater than Volume 2."
    if volume1 < volume2:
        return "Volume 2 is greater than Volume 1."
    
    return "Both volumes are equal."

if __name__ == '__main__':
    sample_volume1 = 85.6
    sample_volume2 = 85.6
    result = compare_volumes(sample_volume1, sample_volume2)
    print(result)