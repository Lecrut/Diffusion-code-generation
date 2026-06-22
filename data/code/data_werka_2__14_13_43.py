def validate_volume(volume):
    if not isinstance(volume, (int, float)):
        raise ValueError("Volume must be a number.")

def compare_volumes(volume1: float, volume2: float) -> str:
    validate_volume(volume1)
    validate_volume(volume2)
    
    if volume1 > volume2:
        return "Volume 1 is greater than Volume 2."
    elif volume1 < volume2:
        return "Volume 2 is greater than Volume 1."
    else:
        return "Both volumes are equal."

if __name__ == '__main__':
    sample_volume1 = 85.6
    sample_volume2 = 23.4
    comparison_result = compare_volumes(sample_volume1, sample_volume2)
    print(comparison_result)