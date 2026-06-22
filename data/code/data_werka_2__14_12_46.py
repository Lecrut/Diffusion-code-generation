def compare_volumes(volume1, volume2):
    if not isinstance(volume1, (int, float)) or not isinstance(volume2, (int, float)):
        raise ValueError("Both volumes must be numbers.")
    
    difference = volume1 - volume2
    
    if difference > 0:
        return "First volume is greater than the second."
    elif difference < 0:
        return "First volume is less than the second."
    else:
        return "Both volumes are equal."

if __name__ == '__main__':
    sample_volume1 = 6.28318
    sample_volume2 = 3.14159
    
    result = compare_volumes(sample_volume1, sample_volume2)
    print(result)