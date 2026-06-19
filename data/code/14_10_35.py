def compare_volumes(volume1, volume2):
    if volume1 > volume2:
        return "Volume 1 is larger"
    elif volume1 < volume2:
        return "Volume 2 is larger"
    else:
        return "Volumes are equal"

if __name__ == '__main__':
    volume_a = 500.75
    volume_b = 300.50
    result = compare_volumes(volume_a, volume_b)
    print(result)