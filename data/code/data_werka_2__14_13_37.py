def compare_volumes(volume1: float, volume2: float) -> str:
    if not isinstance(volume1, (int, float)) or not isinstance(volume2, (int, float)):
        raise ValueError("Both volumes must be numbers.")
    
    if volume1 > volume2:
        return "Volume 1 is greater than Volume 2."
    elif volume1 < volume2:
        return "Volume 2 is greater than Volume 1."
    else:
        return "Both volumes are equal."

if __name__ == '__main__':
    first_volume = 85.6
    second_volume = 23.4
    comparison_result = compare_volumes(first_volume, second_volume)
    print(comparison_result)