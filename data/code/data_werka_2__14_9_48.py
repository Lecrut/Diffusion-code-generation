def compare_volumes(volume1, volume2):
    if not isinstance(volume1, (int, float)) or not isinstance(volume2, (int, float)):
        raise ValueError("Both volumes must be numbers")
    
    larger_volume = max(volume1, volume2)
    smaller_volume = min(volume1, volume2)
    
    if larger_volume == smaller_volume:
        return "Volumes are equal"
    elif larger_volume == volume1:
        return "Volume 1 is larger"
    else:
        return "Volume 2 is larger"

if __name__ == '__main__':
    sample_volume1 = 100.5
    sample_volume2 = 100.5
    try:
        result = compare_volumes(sample_volume1, sample_volume2)
        print(result)
    except ValueError as e:
        print(e)