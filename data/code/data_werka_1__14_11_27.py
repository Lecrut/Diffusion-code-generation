def compare_volumes(volume1, volume2):
    if volume1 > volume2:
        return f"Volume 1 ({volume1}) is greater than Volume 2 ({volume2})."
    elif volume1 < volume2:
        return f"Volume 2 ({volume2}) is greater than Volume 1 ({volume1})."
    else:
        return "Both volumes are equal."

if __name__ == '__main__':
    volume1 = 500
    volume2 = 750
    result = compare_volumes(volume1, volume2)
    print(result)