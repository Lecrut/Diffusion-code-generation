def compare_volumes(volume1, volume2):
    if not isinstance(volume1, (float, int)) or not isinstance(volume2, (float, int)):
        raise ValueError("Both volumes must be numbers.")
    
    larger = max(volume1, volume2)
    smaller = min(volume1, volume2)
    difference = abs(volume1 - volume2)
    return larger, smaller, difference

if __name__ == '__main__':
    SAMPLE_VOLUME_1 = 5.2
    SAMPLE_VOLUME_2 = 7.8
    result = compare_volumes(SAMPLE_VOLUME_1, SAMPLE_VOLUME_2)
    print(result)