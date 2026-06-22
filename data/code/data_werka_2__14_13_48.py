def compare_volumes(volume1: float, volume2: float) -> str:
    if not isinstance(volume1, (int, float)) or not isinstance(volume2, (int, float)):
        raise ValueError("Both volumes must be numbers.")
    
    def determine_magnitude(v1, v2):
        if v1 > v2:
            return "Volume 1 is greater than Volume 2."
        elif v1 < v2:
            return "Volume 2 is greater than Volume 1."
        else:
            return "Both volumes are equal."
    
    return determine_magnitude(volume1, volume2)

if __name__ == '__main__':
    sample_volume1 = 45.6
    sample_volume2 = 89.1
    result = compare_volumes(sample_volume1, sample_volume2)
    print(result)