def compare_volumes(volume1, volume2):
    if not isinstance(volume1, (int, float)) or not isinstance(volume2, (int, float)):
        raise ValueError("Both volumes must be numbers")
    
    if volume1 > volume2:
        return "Volume 1 is greater than Volume 2"
    elif volume1 < volume2:
        return "Volume 1 is less than Volume 2"
    else:
        return "Both volumes are equal"

if __name__ == '__main__':
    volume1 = 100.5
    volume2 = 200.3
    result = compare_volumes(volume1, volume2)
    print(result)