def compare_volumes(volume1, volume2):
    if not isinstance(volume1, (int, float)) or not isinstance(volume2, (int, float)):
        raise ValueError("Both volumes must be numbers.")
    
    original_volumes = {
        "volume1": volume1,
        "volume2": volume2
    }
    
    if volume1 == volume2:
        ratio = 1.0
        are_equal = True
    else:
        larger_volume = max(volume1, volume2)
        smaller_volume = min(volume1, volume2)
        ratio = larger_volume / smaller_volume
        are_equal = False
    
    result = {
        "original_volumes": original_volumes,
        "ratio": ratio,
        "are_equal": are_equal
    }
    
    return result

if __name__ == '__main__':
    sample_volume1 = 250.0
    sample_volume2 = 100.0
    print(compare_volumes(sample_volume1, sample_volume2))