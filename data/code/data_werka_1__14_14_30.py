def compare_volumes(volume1, volume2):
    if not isinstance(volume1, (int, float)) or not isinstance(volume2, (int, float)):
        raise TypeError("Both volumes must be numbers")
    
    if volume1 > volume2:
        return "Volume 1 is greater than Volume 2"
    elif volume1 < volume2:
        return "Volume 2 is greater than Volume 1"
    else:
        return "Both volumes are equal"

if __name__ == '__main__':
    sample_volume1 = 150.5
    sample_volume2 = 200.3
    result = compare_volumes(sample_volume1, sample_volume2)
    print(result)