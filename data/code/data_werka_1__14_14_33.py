def compare_volumes(volume1, volume2):
    if not isinstance(volume1, (int, float)) or not isinstance(volume2, (int, float)):
        raise TypeError("Both arguments must be numbers")
    
    if volume1 > volume2:
        return "Volume 1 is greater than Volume 2"
    elif volume1 < volume2:
        return "Volume 1 is less than Volume 2"
    else:
        return "Both volumes are equal"

if __name__ == '__main__':
    volume_a = 50.5
    volume_b = 30.2
    result = compare_volumes(volume_a, volume_b)
    print(result)