def compare_volumes(volume1: float, volume2: float) -> str:
    if volume1 > volume2:
        return "Volume 1 is greater than Volume 2"
    elif volume1 < volume2:
        return "Volume 2 is greater than Volume 1"
    else:
        return "Both volumes are equal"

if __name__ == '__main__':
    volume_a = 50.5
    volume_b = 30.3
    result = compare_volumes(volume_a, volume_b)
    print(result)