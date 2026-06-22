def validate_volume(volume):
    if not isinstance(volume, (int, float)):
        raise ValueError("Volume must be a number.")

def compare_volumes(volume1, volume2):
    validate_volume(volume1)
    validate_volume(volume2)
    
    if volume1 > volume2:
        return "First volume is greater than the second."
    elif volume1 < volume2:
        return "First volume is less than the second."
    else:
        return "Both volumes are equal."

if __name__ == '__main__':
    volume1 = 6.28318
    volume2 = 3.14159
    result = compare_volumes(volume1, volume2)
    print(result)