def compare_volumes(volume1, volume2):
    if volume1 > volume2:
        return f"Volume 1 ({volume1}) is greater than Volume 2 ({volume2})."
    elif volume1 < volume2:
        return f"Volume 1 ({volume1}) is less than Volume 2 ({volume2})."
    else:
        return "Both volumes are equal."

if __name__ == '__main__':
    volume_a = 100.5
    volume_b = 75.3
    result = compare_volumes(volume_a, volume_b)
    print(result)