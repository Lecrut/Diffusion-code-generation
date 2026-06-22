VOLUME_THRESHOLD = 0

def compare_volumes(volume1, volume2):
    if abs(volume1 - volume2) < VOLUME_THRESHOLD:
        return "Both volumes are essentially equal."
    elif volume1 > volume2:
        return f"Volume 1 ({volume1}) is greater than Volume 2 ({volume2})."
    else:
        return f"Volume 2 ({volume2}) is greater than Volume 1 ({volume1})."

if __name__ == '__main__':
    VOLUME_A = 600
    VOLUME_B = 650
    comparison_result = compare_volumes(VOLUME_A, VOLUME_B)
    print(comparison_result)