def compare_volumes(volume1, volume2):
    if not isinstance(volume1, (int, float)) or not isinstance(volume2, (int, float)):
        raise TypeError("Both volumes must be numbers.")
    
    if volume1 > volume2:
        return "volume1 is greater than volume2"
    elif volume1 < volume2:
        return "volume1 is less than volume2"
    else:
        return "volume1 is equal to volume2"

if __name__ == '__main__':
    sample_volume1 = 500.5
    sample_volume2 = 300.75
    result = compare_volumes(sample_volume1, sample_volume2)
    print(result)