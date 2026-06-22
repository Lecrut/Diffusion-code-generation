def calculate_volume_ratio(volume1, volume2):
    if volume1 <= 0 or volume2 <= 0:
        raise ValueError("Volumes must be positive numbers.")
    
    larger_volume = max(volume1, volume2)
    smaller_volume = min(volume1, volume2)
    
    ratio = larger_volume / smaller_volume
    are_equal = volume1 == volume2
    
    return {
        'volume1': volume1,
        'volume2': volume2,
        'ratio': ratio,
        'are_equal': are_equal
    }

if __name__ == '__main__':
    sample_volume1 = 50.0
    sample_volume2 = 25.0
    
    result = calculate_volume_ratio(sample_volume1, sample_volume2)
    print(result)