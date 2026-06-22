VOLUME_TOLERANCE = 1e-9

def compare_volumes(volume1: float, volume2: float) -> str:
    if not isinstance(volume1, (int, float)) or not isinstance(volume2, (int, float)):
        raise ValueError("Both volumes must be numbers.")
    
    if abs(volume1 - volume2) < VOLUME_TOLERANCE:
        return "Both volumes are equal."
    elif volume1 > volume2:
        return "Volume 1 is greater than Volume 2."
    else:
        return "Volume 2 is greater than Volume 1."

if __name__ == '__main__':
    sample_volume1 = 45.6
    sample_volume2 = 23.4
    comparison_result = compare_volumes(sample_volume1, sample_volume2)
    print(comparison_result)