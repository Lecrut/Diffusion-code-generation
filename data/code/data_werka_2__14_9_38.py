def compare_volumes(volume1, volume2):
    if not isinstance(volume1, (int, float)) or not isinstance(volume2, (int, float)):
        raise ValueError("Both volumes must be numbers")
    
    larger_volume = max(volume1, volume2)
    smaller_volume = min(volume1, volume2)
    
    if volume1 == volume2:
        return "Volumes are equal"
    elif volume1 == larger_volume:
        return "Volume 1 is larger"
    else:
        return "Volume 2 is larger"

if __name__ == '__main__':
    sample_volume1 = 250.75
    sample_volume2 = 200.25
    try:
        comparison_result = compare_volumes(sample_volume1, sample_volume2)
        print(comparison_result)
    except ValueError as e:
        print(e)