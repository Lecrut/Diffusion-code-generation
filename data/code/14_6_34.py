def compare_volumes(volume1, volume2):
    larger = max(volume1, volume2)
    smaller = min(volume1, volume2)
    difference = abs(volume1 - volume2)
    return (larger, smaller, difference)

if __name__ == '__main__':
    sample_volume1 = 34.5
    sample_volume2 = 45.67
    result = compare_volumes(sample_volume1, sample_volume2)
    print(result)