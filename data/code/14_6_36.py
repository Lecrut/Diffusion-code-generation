def compare_volumes(volume1, volume2):
    if volume1 > volume2:
        larger = volume1
        smaller = volume2
    else:
        larger = volume2
        smaller = volume1
    difference = abs(volume1 - volume2)
    return larger, smaller, difference

if __name__ == '__main__':
    sample_volume1 = 5.678
    sample_volume2 = 2.345
    result = compare_volumes(sample_volume1, sample_volume2)
    print(result)