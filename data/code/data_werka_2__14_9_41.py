def validate_volume(volume):
    if not isinstance(volume, (int, float)):
        raise ValueError("Volume must be a number")

def compare_volumes(volume1, volume2):
    validate_volume(volume1)
    validate_volume(volume2)
    
    if volume1 > volume2:
        return "Volume 1 is larger"
    elif volume1 < volume2:
        return "Volume 2 is larger"
    else:
        return "Volumes are equal"

if __name__ == '__main__':
    sample_volume1 = 100.0
    sample_volume2 = 85.5
    try:
        result = compare_volumes(sample_volume1, sample_volume2)
        print(result)
    except ValueError as e:
        print(e)