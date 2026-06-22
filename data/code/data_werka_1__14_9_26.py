def calculate_volume_ratio(volume1, volume2):
    volumes = {
        'volume1': volume1,
        'volume2': volume2
    }
    
    if volume1 == volume2:
        volumes['ratio'] = 1.0
        volumes['are_equal'] = True
    else:
        larger_volume = max(volume1, volume2)
        smaller_volume = min(volume1, volume2)
        volumes['ratio'] = larger_volume / smaller_volume
        volumes['are_equal'] = False
    
    return volumes

if __name__ == '__main__':
    sample_volume1 = 50.0
    sample_volume2 = 25.0
    result = calculate_volume_ratio(sample_volume1, sample_volume2)
    print(result)