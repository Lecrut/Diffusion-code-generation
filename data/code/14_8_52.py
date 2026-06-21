def compare_volumes(volume1, volume2):
    if not isinstance(volume1, (int, float)) or not isinstance(volume2, (int, float)):
        raise ValueError("Both volumes must be numbers.")
    
    original_volumes = {
        "volume1": volume1,
        "volume2": volume2
    }
    
    are_equal = volume1 == volume2
    
    if are_equal:
        ratio = 1.0
    else:
        larger_volume = max(volume1, volume2)
        smaller_volume = min(volume1, volume2)
        if smaller_volume == 0:
            ratio = float('inf')
        else:
            ratio = larger_volume / smaller_volume
    
    return {
        "original_volumes": original_volumes,
        "ratio": ratio,
        "are_equal": are_equal
    }

if __name__ == '__main__':
    sample_volume1 = 75.0
    sample_volume2 = 30.0
    result = compare_volumes(sample_volume1, sample_volume2)
    print(result)