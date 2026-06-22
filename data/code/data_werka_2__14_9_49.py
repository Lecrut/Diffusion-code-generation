def compare_volumes(volume1, volume2):
    if not isinstance(volume1, (int, float)) or not isinstance(volume2, (int, float)):
        raise ValueError("Both volumes must be numbers")
    
    if volume1 > volume2:
        return "Volume 1 is larger"
    if volume1 < volume2:
        return "Volume 2 is larger"
    return "Volumes are equal"

if __name__ == '__main__':
    volume1 = 100.0
    volume2 = 50.0
    try:
        result = compare_volumes(volume1, volume2)
        print(result)
    except ValueError as e:
        print(e)