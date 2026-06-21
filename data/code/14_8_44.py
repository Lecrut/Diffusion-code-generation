def compare_volumes(volume1, volume2):
    if not isinstance(volume1, (int, float)) or not isinstance(volume2, (int, float)):
        raise ValueError("Both volumes must be numbers.")
    
    original_volumes = {
        "volume1": volume1,
        "volume2": volume2
    }
    
    ratio = max(volume1, volume2) / min(volume1, volume2)
    are_equal = volume1 == volume2
    
    result = {
        **original_volumes,
        "ratio": ratio,
        "are_equal": are_equal
    }
    
    return result

if __name__ == '__main__':
    sample_volume1 = 50.0
    sample_volume2 = 25.0
    print(compare_volumes(sample_volume1, sample_volume2))