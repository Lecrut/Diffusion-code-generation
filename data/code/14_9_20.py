def compare_volumes(volume1, volume2):
    result = {
        'volume1': volume1,
        'volume2': volume2,
        'ratio': None,
        'are_equal': False
    }
    
    if volume1 == volume2:
        result['are_equal'] = True
    else:
        larger_volume = max(volume1, volume2)
        smaller_volume = min(volume1, volume2)
        result['ratio'] = larger_volume / smaller_volume
    
    return result

if __name__ == '__main__':
    sample_volume1 = 50.0
    sample_volume2 = 25.0
    print(compare_volumes(sample_volume1, sample_volume2))