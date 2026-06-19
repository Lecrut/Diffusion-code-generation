def compare_volumes(volume1, volume2):
    if isinstance(volume1, (int, float)) and isinstance(volume2, (int, float)):
        if volume1 > volume2:
            return "Volume 1 is greater than Volume 2"
        elif volume1 < volume2:
            return "Volume 2 is greater than Volume 1"
        else:
            return "Both volumes are equal"
    else:
        raise TypeError("Both arguments must be numbers (int or float)")

if __name__ == '__main__':
    volume_a = 500.5
    volume_b = 300.75
    result = compare_volumes(volume_a, volume_b)
    print(result)