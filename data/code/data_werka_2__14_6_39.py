def compare_volumes(volume1, volume2):
    larger = max(volume1, volume2)
    smaller = min(volume1, volume2)
    difference = abs(volume1 - volume2)
    return larger, smaller, difference

if __name__ == '__main__':
    SAMPLE_VOLUME_1 = 5.678
    SAMPLE_VOLUME_2 = 3.456
    result = compare_volumes(SAMPLE_VOLUME_1, SAMPLE_VOLUME_2)
    print(result)