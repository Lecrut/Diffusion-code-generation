def validate_volume(volume):
    if not isinstance(volume, (int, float)):
        raise ValueError("Volume must be a number.")
    if volume <= 0:
        raise ValueError("Volume must be positive.")

def compare_volumes(volume1, volume2):
    validate_volume(volume1)
    validate_volume(volume2)
    
    original_volumes = {
        "volume1": volume1,
        "volume2": volume2
    }
    
    larger_volume = max(volume1, volume2)
    smaller_volume = min(volume1, volume2)
    
    ratio = larger_volume / smaller_volume if smaller_volume != 0 else float('inf')
    are_equal = volume1 == volume2
    
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