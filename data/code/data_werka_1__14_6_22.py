def compare_volumes(volume1, volume2):
    larger_volume = max(volume1, volume2)
    smaller_volume = min(volume1, volume2)
    difference = abs(volume1 - volume2)
    return (larger_volume, smaller_volume, difference)

if __name__ == '__main__':
    sample_volume1 = 3.5
    sample_volume2 = 4.8
    result = compare_volumes(sample_volume1, sample_volume2)
    print(result)