def compare_volumes(volume1, volume2):
    if volume1 > volume2:
        return volume1, volume2, abs(volume1 - volume2)
    else:
        return volume2, volume1, abs(volume2 - volume1)

if __name__ == '__main__':
    sample_volume1 = 5.2
    sample_volume2 = 7.8
    result = compare_volumes(sample_volume1, sample_volume2)
    print(result)