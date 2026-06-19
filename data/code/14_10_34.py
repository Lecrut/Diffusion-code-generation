def compare_volumes(volume1, volume2):
    if volume1 > volume2:
        return "Volume 1 is larger"
    elif volume1 < volume2:
        return "Volume 2 is larger"
    else:
        return "Volumes are equal"

if __name__ == '__main__':
    sample_volume1 = 50.0
    sample_volume2 = 75.0
    result = compare_volumes(sample_volume1, sample_volume2)
    print(result)