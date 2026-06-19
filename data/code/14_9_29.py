def compare_volumes(volume1, volume2):
    result = {
        'volume1': volume1,
        'volume2': volume2,
        'ratio': None,
        'are_equal': False
    }
    
    if volume1 > volume2:
        result['ratio'] = volume1 / volume2
    elif volume2 > volume1:
        result['ratio'] = volume2 / volume1
    else:
        result['ratio'] = 1.0
        result['are_equal'] = True
    
    return result

if __name__ == '__main__':
    sample_volume1 = 500.0
    sample_volume2 = 250.0
    print(compare_volumes(sample_volume1, sample_volume2))