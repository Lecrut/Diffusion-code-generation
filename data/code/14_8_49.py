def compare_volumes(volume1, volume2):
    if not isinstance(volume1, (int, float)) or not isinstance(volume2, (int, float)):
        raise ValueError("Both volumes must be numbers.")
    
    original_volumes = {
        "volume1": volume1,
        "volume2": volume2
    }
    
    if volume1 == volume2:
        return {
            **original_volumes,
            "ratio": 1.0,
            "are_equal": True
        }
    
    larger_volume = max(volume1, volume2)
    smaller_volume = min(volume1, volume2)
    
    if smaller_volume == 0:
        ratio = float('inf')
    else:
        ratio = larger_volume / smaller_volume
    
    return {
        **original_volumes,
        "ratio": ratio,
        "are_equal": False
    }

if __name__ == '__main__':
    sample_volume1 = 75.0
    sample_volume2 = 30.0
    result = compare_volumes(sample_volume1, sample_volume2)
    print(result)