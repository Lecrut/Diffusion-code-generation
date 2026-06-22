def compare_volumes(volume1, volume2):
    volumes = {'volume1': volume1, 'volume2': volume2}
    if volume1 == volume2:
        ratio = 1.0
    else:
        larger_volume = max(volume1, volume2)
        smaller_volume = min(volume1, volume2)
        ratio = larger_volume / smaller_volume
    volumes['ratio'] = ratio
    volumes['are_equal'] = volume1 == volume2
    return volumes

if __name__ == '__main__':
    sample_volume1 = 100.0
    sample_volume2 = 50.0
    result = compare_volumes(sample_volume1, sample_volume2)
    print(result)