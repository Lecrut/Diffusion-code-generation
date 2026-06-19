def compare_volumes(volume1, volume2):
    if volume1 > volume2:
        return f"Volume 1 ({volume1}) is greater than Volume 2 ({volume2})."
    elif volume1 < volume2:
        return f"Volume 2 ({volume2}) is greater than Volume 1 ({volume1})."
    else:
        return "Both volumes are equal."

if __name__ == '__main__':
    volume_a = 500
    volume_b = 300
    result = compare_volumes(volume_a, volume_b)
    print(result)