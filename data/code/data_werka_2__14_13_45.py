def is_valid_volume(volume):
    return isinstance(volume, (int, float))

def compare_volumes(volume1: float, volume2: float) -> str:
    if not is_valid_volume(volume1) or not is_valid_volume(volume2):
        raise ValueError("Both volumes must be numbers.")
    
    if volume1 > volume2:
        return "Volume 1 is greater than Volume 2."
    elif volume1 < volume2:
        return "Volume 2 is greater than Volume 1."
    else:
        return "Both volumes are equal."

if __name__ == '__main__':
    sample_volume1 = 80.5
    sample_volume2 = 60.3
    result = compare_volumes(sample_volume1, sample_volume2)
    print(result)