def compare_volumes(volume1, volume2):
    if not isinstance(volume1, (int, float)) or not isinstance(volume2, (int, float)):
        raise ValueError("Both volumes must be numbers.")
    
    if volume1 > volume2:
        return f"Volume 1 ({volume1}) is greater than Volume 2 ({volume2})."
    elif volume1 < volume2:
        return f"Volume 2 ({volume2}) is greater than Volume 1 ({volume1})."
    else:
        return "Both volumes are equal."

if __name__ == '__main__':
    VOLUME_A = 600
    VOLUME_B = 450
    try:
        result = compare_volumes(VOLUME_A, VOLUME_B)
        print(result)
    except ValueError as e:
        print(e)